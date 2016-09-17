#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys

class ListImage(object):
  def __init__(self, searchDir):
    self.searchDir = searchDir
    print('init ListImage searchDir: %s' % searchDir)
  def images(self):
    drawableDirs = self.__list_drawable_dir()
    imageFiles = [y for x in map(self.__list_files, drawableDirs) for y in x]
    return imageFiles

  def __list_drawable_dir(self):
    return [x for x in os.listdir(self.searchDir) if os.path.isdir(os.path.join(self.searchDir, x)) and (x.startswith('drawable') or x.startswith('mipmap'))]

  def __list_files(self, d):
    baseDir = os.path.join(self.searchDir, d)
    return [os.path.join(baseDir, x) for x in os.listdir(baseDir) if os.path.isfile(os.path.join(baseDir, x)) and self.is_image(x)]

  def is_image(self, file):
    return file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')

if __name__ == '__main__':
  print('===execute ListImage from console===')
  searchDir = './app/src/main/res'
  if len(sys.argv) == 2:
    searchDir = sys.argv[1]
    print('from input searchDir:', searchDir)

  LI = ListImage(searchDir)
  print('searched images======>\n', LI.images())