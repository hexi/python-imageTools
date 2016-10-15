#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys
from listdrawable import ListDrawable

class ListImage(object):
  def __init__(self, searchDir):
    self.searchDir = searchDir
    print('init ListImage searchDir: %s' % searchDir)
  def images(self):
    drawableDirs = ListDrawable(self.searchDir).search()
    imageFiles = [y for x in map(self.__list_files, drawableDirs) for y in x]
    return imageFiles

  def __list_files(self, d):
    baseDir = d
    return [os.path.join(baseDir, x) for x in os.listdir(baseDir) if os.path.isfile(os.path.join(baseDir, x)) and self.is_image(x)]

  def is_image(self, file):
    return file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')

if __name__ == '__main__':
  print('===execute ListImage from console===')
  searchDir = './app/src/main/res'
  if len(sys.argv) == 2:
    searchDir = sys.argv[1]
    print('from input searchDir:', searchDir)

  images = ListImage(searchDir).images()
  print('searched %d images======>\n%s' % (len(images), images))