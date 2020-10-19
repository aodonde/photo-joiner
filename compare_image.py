import sys
from PIL import Image

infile1 = Image.open("pic1.png")
infile2 = Image.open("pic2.png")
infile3 = Image.open("pic1.png")

out1 = Image.blend(infile1,infile2,0.5)

r, g, b = infile3.split()

infile3 = Image.merge("RGB", (b, g, r))
out2 = infile3


out3 = Image.blend(infile2,infile3,0.5)


out1.save('new1.png')
out2.save('new2.png')
out3.save('new3.png')
