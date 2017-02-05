from PIL import Image
import os
import imageio
import db
import config

def generate():
    size = (300, 300)

    input_filenames = []
    output_filename = config.upload_dir(config.GIF_FILE)

    # Load images from db
    for item in db.get_items():
        if item.get('photo'):
            input_filenames.append(config.upload_dir(item.get('photo')))

    # Create thumbnails
    for filename in input_filenames:
        image = Image.open(filename).convert('RGB')
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)

    # Open and store images
    input_images = [imageio.imread(fn) for fn in input_filenames]

    # Generate
    imageio.mimsave(output_filename, input_images, duration=0.3)

def remove():
    filename = config.upload_dir(config.GIF_FILE)
    try:
        os.remove(filename)
    except OSError:
        pass
