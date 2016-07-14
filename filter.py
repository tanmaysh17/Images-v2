import sys
from PIL import Image


def getpixel(pic, x, y):
    w, h = pic.size
    curr_pixel = pic.load()
    if x < 0:
        x = 0
    if x >= w:
        x = w-1
    if y < 0:
        y = 0
    if y >= h:
        y = h-1
    return curr_pixel[x, y]


def region3x3(pic, x, y):
    NW = getpixel(pic, x-1, y-1)
    N = getpixel(pic, x, y-1)
    NE = getpixel(pic, x+1, y-1)
    W = getpixel(pic, x-1, y)
    C = getpixel(pic, x, y)
    E = getpixel(pic, x+1, y)
    SW = getpixel(pic, x-1, y+1)
    S = getpixel(pic, x, y+1)
    SE = getpixel(pic, x+1, y+1)

    return [NW, N, NE, W, C, E, SW, S, SE]


def filter(pic, f):
    width, height = pic.size
    newpic = pic.copy()
    new_pixel = newpic.load()

    for i in range(0, height):
        for j in range(0, width):

            new_pixel[j, i] = f(region3x3(pic, j, i))

    return newpic


def open(argv):
    if len(argv) != 2:
        print "$ python View.py filename"
        sys.exit(1)

    filename = argv[1]
    img = Image.open(filename)

    return img


