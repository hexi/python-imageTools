#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from PIL import ImageChops, Image
import math, operator
import sys
from functools import reduce
from ListImage import ListImage
import os

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    image1 = Image.open(im1)
    image2 = Image.open(im2)

    # try:
    #   h = ImageChops.difference(image1, image2).histogram()

    #   # calculate rms
    #   return math.sqrt(reduce(operator.add,
    #       map(lambda h, i: h*(i**2), h, range(256))
    #   ) / (float(image1.size[0]) * image1.size[1]))

    # except Exception as e:
    #   raise e
    # finally:
    #   image1.close()
    #   image2.close()

    try:
      h1 = image1.histogram()
      h2 = image2.histogram()

      return math.sqrt(reduce(operator.add,
          map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    except Exception as e:
      raise e
    finally:
      image1.close()
      image2.close()
      
def issameimage(im1, im2):
  return rmsdiff(im1, im2) == 0

if __name__ == '__main__':
  if len(sys.argv) == 3:
    im1 = sys.argv[1]
    im2 = sys.argv[2]
    print('im1: {im1}, im2: {im2}'.format(im1=im1, im2=im2))
    print('===is same image:', issameimage(im1, im2))

  elif len(sys.argv) <= 2:
    baseDir = os.path.abspath('.')
    if len(sys.argv) == 2:
      baseDir = sys.argv[1]
    
    #find all images in specified path
    listImage = ListImage(baseDir)
    imageFiles = listImage.images()

    #group images by file size
    groupBySizeDict = {}
    for imageFile in imageFiles:
      fileSize = os.stat(imageFile).st_size
      if not str(fileSize) in groupBySizeDict:
        groupBySizeDict[str(fileSize)] = list()

      groupBySizeDict[str(fileSize)].append(imageFile)

    #find the same images in same group
    for files in groupBySizeDict.values():
      if len(files) < 2:
        continue
      size = len(files)
      for i in range(0, size - 1):
        currentImage = files[i]
        for j in range(i+1, size):
          targetImage = files[j]
          if issameimage(currentImage, targetImage):
            print('===samge image:%s, %s' % (currentImage, targetImage))




