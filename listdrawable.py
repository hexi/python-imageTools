#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import sys

class ListDrawable(object):
	blacklist = ['build', 'libs', 'androidTest', 'assets', 'test', 'gradle', '.gradle', '.idea', '.git']

	def __init__(self, searchDir):
		super(ListDrawable, self).__init__()
		self.searchDir = searchDir
		print('init ListDrawable searchDir: %s' % searchDir)

	def search(self):
		drawableDirs = list()
		baseDir = self.searchDir
		self.__find_drawables(drawableDirs, baseDir)
		return drawableDirs


	def __find_drawables(self, listResult, currentPath):
		if not os.path.isdir(currentPath):
			return
		if self.__is_in_blacklist(currentPath):
			return
		if self.__is_drawable_dir(currentPath):
			listResult.append(currentPath)
			return
		for d in os.listdir(currentPath):
			tmpPath = os.path.join(currentPath, d)
			if not os.path.isdir(tmpPath):
				continue
			self.__find_drawables(listResult, tmpPath)

	def __is_drawable_dir(self, folder):
		head, tail = os.path.split(folder)
		return (tail.startswith('drawable') or tail.startswith('mipmap'))

	def __is_in_blacklist(self, folder):
		head, tail = os.path.split(folder)
		inBlacklist = False
		try:
			index = ListDrawable.blacklist.index(tail)
			inBlacklist = index >= 0
		except Exception as e:
			inBlacklist = False

		return inBlacklist

if __name__ == '__main__':
  searchDir = '.'
  if len(sys.argv) == 2:
    searchDir = sys.argv[1]
    print('from input searchDir:', searchDir)

  dawables = ListDrawable(searchDir).search()
  print('searched images======>\n', dawables)
