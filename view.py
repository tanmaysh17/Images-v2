import sys
from PIL import Image

if len(sys.argv) != 2:
    print "$ python View.py filename"
    sys.exit(1)

filename = sys.argv[1]
img = Image.open(filename)
img = img.convert('L')
img.show()