#!/usr/bin/env python
# coding=utf-8
import os
import sys

import StringIO
#import Image
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf-8')

def ensure_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

def crop_image(tfilename):
    MAXSIZEX = 1242 
    MAXSIZEY = 2208
    ratio = 1. * MAXSIZEX / MAXSIZEY

    print tfilename

    im = Image.open(tfilename)
    (width, height) = im.size

    if width > height * ratio:
        newwidth = int(height * ratio)
        left = width / 2 - newwidth / 2
        right = left + newwidth
        top = 0
        bottom = height

    if width != height * ratio:
        im = im.crop((left, top, right, bottom))

    im = im.resize((MAXSIZEX, MAXSIZEY), Image.ANTIALIAS)
    im.save(tfilename, "jpeg", quality = 80)

files = os.listdir(".")

for filename in files:
    portion = os.path.splitext(filename)
    newname = portion[0] + ".jpg"
    if not portion[1]:
        crop_image(filename)
        os.rename(filename, newname)

