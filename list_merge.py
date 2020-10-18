import sys
import glob
import math
from PIL import Image

png_image_list = [f for f in glob.glob("*.png")]

image_list = [ Image.open(x) for x in png_image_list ]
width,height = zip(*(i.size for i in image_list))

total_width = sum(width)
max_height = max(height)

#rows = (math.trunc((len(image_list)/4))) + 1
#print(rows)


container_img = Image.new('RGB', (total_width, max_height))

x_offset = 0
y_offset = 0
for i in image_list:
    container_img.paste(i, (x_offset,0))
    x_offset += i.size[0]

container_img.save('new2.png')



