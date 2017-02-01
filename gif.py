from images2gif import writeGif
from PIL import Image, ImageSequence
import os
import db
import config

def generate():
    images = []
    size = (600,350)
    filename = config.upload_dir('loading.gif')
    for item in db.get_items():
        if item.photo:
            image = Image.open(config.upload_dir(item.photo))
            image.thumbnail(size, Image.ANTIALIAS)
            images.append(image)
    writeGif(filename, images, duration=0.5, subRectangles=False)
