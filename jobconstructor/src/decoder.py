
import os

from . import exceptions

class Decoder(object):
	def __init__(self, rootpath, title):
		self.rootpath = rootpath
		self.title = title
		self.validate_rootpath()

	def validate_rootpath(self):
		if not os.path.exists(self.rootpath):
			raise exceptions.JobConstructorException("Warehouse [{0}] couldn't be located".format(self.rootpath))

	def get_package_name(self):
		# Getting list of all subdirectories (packages) in rootpath
		subdirs = [subdir for subdir in os.listdir(self.rootpath) if os.path.isdir(os.path.join(self.rootpath, subdir))]

		# Getting required package name
		test_name = max(set(os.path.commonprefix([subdir, self.title]) for subdir in subdirs)).rstrip('_-')

		if test_name not in subdirs:
			raise exceptions.JobConstructorException("Test package [{0}] couldn't be located".format(test_name))

		return test_name
