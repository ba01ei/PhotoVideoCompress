#!/usr/bin/env python

import os
import re
import sys
import math
import subprocess

INPUT_VIDEO_TYPE = ".mov" # the extension name for input videos
INPUT_IMAGE_TYPE = ".jpg" # the extension name for input videos
BIT_RATE = 2000 # the bit rate for compressed videos
JPG_SIDE_LENGTH = 1024  # the approximate length of the longer side, for compressed jpgs
JPG_QUALITY = 80 # the image quality for compressed jpgs


foldername = ""
newfoldername = ""

try:
    foldername = sys.argv[1]
except:
    print("please provide a folder name")

movies = []
pics = []
if len(foldername):
    foldername = os.path.abspath(foldername)
    newfoldername = os.path.normpath(foldername) + "_small"
    os.system("mkdir -p \"%s\"" % newfoldername)

    files = os.listdir(foldername)
    
    for f in files:
        fileName, fileExtension = os.path.splitext(f)
        if fileExtension.lower() == INPUT_VIDEO_TYPE:
            movies.append(f)
        if fileExtension.lower() == INPUT_IMAGE_TYPE:
            pics.append(f)

for pic in pics:
    old_path = os.path.join(foldername, pic)
    noext = os.path.splitext(pic)[0]
    new_path = os.path.join(newfoldername, noext + "_small.jpg")
    p = subprocess.Popen(["identify", old_path], stdout=subprocess.PIPE)
    info = p.stdout.read()
    retcode = p.wait()
    if retcode == 0:
        dimension = re.search("(\d+)x(\d+)", info).groups(0)
        sidelen = max(int(dimension[0]), int(dimension[1]))
        pct = int(math.ceil(JPG_SIDE_LENGTH * 100 / sidelen)) + 1
    else:
        pct = 100

    if pct < 100:
        # scaling by 1M/size on 2-3MB jpgs (40-50%) typically yields jpgs with 600-800k
        # change quality to 80% makes the file ~250k
        cmd = "convert \"%s\" -resize %d%% -quality %d \"%s\"" % (old_path, pct, JPG_QUALITY, new_path)
    else:
        cmd = "cp \"%s\" \"%s\"" % (old_path, new_path)
    print(cmd)
    os.system(cmd)

for mov in movies:
    noext = os.path.splitext(mov)[0]
    mp4 = noext + ("_%dkbps.mp4" % BIT_RATE)
    mov_path = os.path.join(foldername, mov)
    mp4_path = os.path.join(newfoldername, mp4)
    cmd = "HandBrakeCLI -i \"%s\" -o \"%s\" -b %d -e x264 -r 24" % (mov_path, mp4_path, BIT_RATE)
    print(cmd)
    os.system(cmd)



