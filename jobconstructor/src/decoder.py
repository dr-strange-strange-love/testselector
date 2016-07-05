
import os
import sys

class Decoder():
	def __init__(self, rootpath, title):
		self.rootpath = rootpath
		self.title = title

	def check_rootpath(self):
		retval = os.getcwd()
		print '> Current working directory: %s' % retval

		# Trying to enter warehouse (rootpath)
		try:
			os.chdir(self.rootpath)
		except OSError as e:
			print 'Rootpath not found. Exiting program...'
			sys.exit(e)
		retval = os.getcwd()
		print '> Warehouse entered successfully: %s' % retval
		return 1

	def get_package_name(self):
		# Getting list of all subdirectories (packages) in rootpath
		subdirs = [subdir for subdir in os.listdir(self.rootpath) if os.path.isdir(os.path.join(self.rootpath, subdir))]
		print '> Warehouse subdirectories: %s' % subdirs

		# Getting required package name
		test_name = max(set(os.path.commonprefix([subdir, self.title]) for subdir in subdirs)).rstrip('_')
		print '> Lcp: %s' % test_name

		if test_name not in subdirs:
			sys.exit('Package not found in rootpath')

		return test_name
