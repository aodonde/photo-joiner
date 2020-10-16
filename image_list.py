import sys
import glob
from PIL import Image

#print("----- 3 -----\n")
for infile in sys.argv[1:]:
    #print("----- 2 -----\n")
    try:
        with Image.open(infile) as im:
            #print("----- 1 -----\n")
            print(infile, im.format, f"{im.size} x {im.mode}")
    except OSError:
        pass


mylist = [f for f in glob.glob("*.png")]

for infile in mylist:
    print(infile)


#print(mylist)

