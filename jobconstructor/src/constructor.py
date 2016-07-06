
import imp

from . import decoder
from . import builder

class Constructor():
	def __init__(self, rootpath, title):
		self.rootpath = rootpath
		self.title = title
		self.job_dict = {}

	def construct(self):
		dcdr = decoder.Decoder(self.rootpath, self.title)
		# Checking rootpath
		if (dcdr.check_rootpath() == -1):
			return -1 # Warehouse doesn't exist
		# Getting required package name
		test_name = dcdr.get_package_name()
		if (test_name == -2):
			return -2 # Package (test_name) not found in warehouse

		# Importing required package
		try:
			commons_info = imp.find_module(test_name, [self.rootpath])
			commons = imp.load_module(test_name, commons_info[0], commons_info[1], commons_info[2])
		except ImportError as e:
			return -3 # Package couldn't be imported
		# print '> Package imported successfully: %s' % commons

		# Importing required module
		try:
			specifics_info = imp.find_module(self.title, commons.__path__)
			specifics = imp.load_module(self.title, specifics_info[0], specifics_info[1], specifics_info[2])
		except ImportError as e:
			return -4 # Module couldn't be imported
		# print '> Module imported successfully: %s' % specifics

		bldr = builder.Builder(commons.params, specifics.params, self.title, test_name)
		bldr.build_cmd()
		self.job_dict = bldr.build_dict()

		return self.job_dict
