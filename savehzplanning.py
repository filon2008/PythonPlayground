#!/usr/bin/env python
# coding=utf-8
import urllib.request
import sys
import os

def savehzplanning(url):
    urls = url.split('image=')
    asciis = urls[1].split('%u')[1:]
    pmsg = ''.join([chr(int(x, 16)) for x in asciis])
    image_url = '/'.join(urls[0].split('/')[:3]) + pmsg
    urllib.request.urlretrieve(image_url, pmsg.split('/')[-1])

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("usage : %s url" % os.path.basename(sys.argv[0]))
    else:
        savehzplanning(sys.argv[1])
