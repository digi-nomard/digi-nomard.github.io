import shutil
import sys
import cv2
import numpy as np
import base64
import json
import datetime
import os
import urllib.request
import re
import requests
import ssl
import certifi
import fitz
import docx
import validators
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pathlib import Path

class Utils:
    def __init__(self):
        pass

    def renameFolderByMDTitle(dir):
        # iterante all subfolders and find all md files
        # rename md file to date(yyyy-mm-dd)-title.md
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".md"):
                    # read md file
                    md_file = os.path.join(root, file)
                    md_file_content = open(md_file, "r", encoding="utf-8").read()
                    # find date, split by space and get first element
                    date = re.search(r"date: (.*)", md_file_content).group(1).split(" ")[0]
                    # find title
                    title = re.search(r"title: (.*)", md_file_content).group(1)
                    # remove special characters (Except -) but keep other languages
                    title = re.sub(r"[^\w\s-]", "", title).strip()
                    # remove spaces and lower
                    title = title.replace(" ", "-").lower()[:40]
                    # get tags
                    # tags_searc = re.search(r"tags: (.*)", md_file_content)
                    # if tags_searc:
                    #     oldTags = tags_searc.group(1)
                    #     newTags = oldTags.replace(' #', ',').replace('#', '')
                    #     # save changes
                    #     md_file_content = md_file_content.replace(oldTags, newTags)
                    #     open(md_file, "w", encoding="utf-8").write(md_file_content)
                    
                    # rename md file
                    newfilename = date + "-" + title + ".md"
                    if file != newfilename:
                        print(f'{file} -> {newfilename}')
                        os.rename(md_file, os.path.join(root, newfilename))


    def deleteFolder(dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)

    def copyFiles(files, dir):
        for source in files:
            filename = os.path.basename(source)
            destination = os.path.join(dir, filename)
            shutil.copy(source, destination)

    def moveFiles(files, dir):
        for source in files:
            filename = os.path.basename(source)
            destination = os.path.join(dir, filename)
            shutil.move(source, destination)

    # copy all subfolers and files (except .md files) to under the target folder
    def copyFolders(source, target):
        for root, dirs, files in os.walk(source):
            for file in files:
                # check extension that is not .md
                if file.endswith(".md") or file.endswith(".json"):
                    continue
                source_file = os.path.join(root, file)
                target_file = source_file.replace(source, target)
                target_dir = os.path.dirname(target_file)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                shutil.copy(source_file, target_file)


    # def copyFolders(source, target):
    #     for root, dirs, files in os.walk(source):
    #         for file in files:
    #             source_file = os.path.join(root, file)
    #             target_file = source_file.replace(source, target)
    #             target_dir = os.path.dirname(target_file)
    #             if not os.path.exists(target_dir):
    #                 os.makedirs(target_dir)
    #             shutil.copy(source_file, target_file)


# main with 2 parms (source dir, destination dir)
if __name__ == "__main__":
    Utils.renameFolderByMDTitle(sys.argv[1])
    Utils.deleteFolder(sys.argv[2])
    Utils.copyFolders(sys.argv[1], sys.argv[2])
