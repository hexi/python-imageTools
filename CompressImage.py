#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
# /usr/local/lib/python3.4/site-packages/PIL
from PIL import Image
import sys
from ListImage import ListImage
import tinify
tinify.key = 'tinify.key'#请改为自己的tinify key

sizeShouldCompress = 1 * 1024

def is_un_compressed(image):
    f9patch = '.9.'
    if image.find(f9patch) > 0:
        return False
    with Image.open(image) as im:
        return im.format == 'PNG' and im.mode != 'L' and im.mode != 'P' and (os.stat(image).st_size >= sizeShouldCompress)

def is_not_png(image):
    with Image.open(image) as im:
        return im.format != 'PNG'

def compress_image(image):
    print('compressing image:', image)
    tinify.from_file(image).to_file(image)

def batch_compress(images):
    print('------------------------start to compress image----------------------')
    for image in images:
        compress_image(image)
    print('------------------------end to compress image----------------------')


if __name__ == '__main__':
    baseDir = os.path.abspath('.')
    shouldCompress = True
    shouldListImags = False
    def paseBaseDirParm(args):
        if len(args) >= 2:
            baseDir = args[1]
            print("from input baseDir: %s" % baseDir)
            return baseDir
        else:
            return os.path.abspath('.');

    def parseSizeShouldCompressPram(args):
        if len(args) >= 3:
            in_size = int(args[2])
            sizeShouldCompress = in_size * 1024
            print("from input sizeShouldCompress: %d" % in_size)
            return sizeShouldCompress
        else:
            return 1 * 1024

    def parseShouldCompressParam(args):
        if len(args) >= 4:
            try:
                shouldCompress = bool(int(args[3]))
                print("from input shouldCompress: %s" % shouldCompress)
                return shouldCompress
            except Exception as e:
                print('!!!! the third parameter must be 0 or 1')
                
        else:
            return True

    def paseShouldListImagesParam(args):
        if len(args) == 5:
            try:
                shouldListImags = bool(int(args[4]))
                print("from input shouldListImags: %s" % shouldListImags)
                return shouldListImags
            except Exception as e:
                print('!!!! the forth parameter must be 0 or 1')
            
        else:
            return False

    baseDir = paseBaseDirParm(sys.argv)
    sizeShouldCompress = parseSizeShouldCompressPram(sys.argv)
    shouldCompress = parseShouldCompressParam(sys.argv)
    shouldListImags = paseShouldListImagesParam(sys.argv)
    
    print('===params, baseDir: %s, sizeShouldCompress:%d, shouldCompress:%s, shouldListImags:%s' % (baseDir, sizeShouldCompress/1024, shouldCompress, shouldListImags))
    listImage = ListImage(baseDir)

    imageFiles = listImage.images()

    uncompressed = list(filter(is_un_compressed, imageFiles))

    unPngFiles = list(filter(is_not_png, imageFiles))

    if shouldListImags:
        print('===searched %d images======>\n%s' % (len(imageFiles), imageFiles))

    print('===uncompressed png %d files --------------------->' % len(uncompressed))
    print(uncompressed)
    print('===jpg or webp %d files ------------------------->' % len(unPngFiles))
    print(unPngFiles)

    if shouldCompress:
        batch_compress(uncompressed)        



