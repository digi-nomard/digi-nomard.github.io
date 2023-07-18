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
                if file.endswith(".md"):
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
    Utils.deleteFolder(sys.argv[2])
    Utils.copyFolders(sys.argv[1], sys.argv[2])
