Media Compress

Summary
=======

Compress image and video files and save 


Requirements
============

Works on Mac OS. Requires:

- imagemagick, which can be installed through:

    sudo brew install imagemagick

- HandBrakeCLI, which can be installed from:

    http://handbrake.fr/downloads2.php

Usage
=====

    python mcompress.py foldername

- Input: a folder with images and videos
Output: a folder named foldername_small which contains compressed images and videos

- By default, this works with photos and videos from iPhone. Output videos are H.264 encoded with 2000kbps bitrate and 24 frame rate. Output images are JPGs with 80% quality and maximum side length of 1024. The settings can be modified in mcompress.py


License
=======

Copyright (c) 2013 Bao Lei

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


