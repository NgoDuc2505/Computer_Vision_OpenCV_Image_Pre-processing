import os
from PIL import Image

def loader(path):
    try:
        img = Image.open(path)
        return img
    except Exception as ex:
        print("Error: Invalid file path!!!!!")
        return None