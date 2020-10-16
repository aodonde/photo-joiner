import sys
import glob
from PIL import Image

png_image_list = [f for f in glob.glob("*.png")]

for infile in png_image_list:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, im.size)
    except OSError:
        pass

