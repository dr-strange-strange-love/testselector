
import os
import sys

class Decoder():
	def __init__(self, rootpath, title):
		self.rootpath = rootpath
		self.title = title

	def check_rootpath(self):
		# Trying to enter warehouse (rootpath)
		try:
			os.chdir(self.rootpath)
		except OSError as e:
			return -1 # Warehouse doesn't exist

		return 0

	def get_package_name(self):
		# Getting list of all subdirectories (packages) in rootpath
		subdirs = [subdir for subdir in os.listdir(self.rootpath) if os.path.isdir(os.path.join(self.rootpath, subdir))]

		# Getting required package name
		test_name = max(set(os.path.commonprefix([subdir, self.title]) for subdir in subdirs)).rstrip('_-')

		if test_name not in subdirs:
			return -2 # Package (test_name) not found in warehouse

		return test_name
