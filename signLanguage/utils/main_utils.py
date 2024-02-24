import os, sys
import yaml 
import base64

from signLanguage.exception import SignException
from signLanguage.logger import logging

def read_yaml_file(file_path):
    try:
        with open(file_path) as yaml_file:
            logging.info("Reading the yaml File")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SignException(e, sys)
    
    
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
