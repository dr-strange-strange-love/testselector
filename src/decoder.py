
import os
import sys

class Decoder():
	def __init__(self, rootpath, title):
		self.rootpath = rootpath
		self.title = title
		self.workpath = ''

	def set_dir_to_rootpath(self):
		retval = os.getcwd()
		print 'Current working directory: %s' % retval

		# Trying to enter warehouse (rootpath)
		try:
			os.chdir(self.rootpath)
		except OSError as e:
			print 'Rootpath not found. Exiting program...'
			sys.exit(e)
		retval = os.getcwd()
		print 'Warehouse entered successfully: %s' % retval

	def get_package_name(self):
		# Getting list of all subdirectories (packages) in rootpath
		subdirs = [subdir for subdir in os.listdir(self.rootpath) if os.path.isdir(os.path.join(self.rootpath, subdir))]
		print 'Warehouse subdirectories: %s' % subdirs

		# Getting required package name
		lcp = max(set(os.path.commonprefix([subdir, self.title]) for subdir in subdirs)).rstrip('_')
		print 'lcp: %s' % lcp

		if lcp not in subdirs:
			sys.exit('Package not found in rootpath')

		return lcp
