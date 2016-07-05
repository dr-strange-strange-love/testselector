
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
		dcdr.check_rootpath()
		# Getting required package name
		test_name = dcdr.get_package_name()

		# !ImportError
		# Importing required package (dynamically)
		commons_info = imp.find_module(test_name, [self.rootpath])
		commons = imp.load_module(test_name, commons_info[0], commons_info[1], commons_info[2])
		print '> Package imported successfully: %s' % commons

		# !ImportError, not too valid module import
		# Importing required module (dynamically)
		specifics_info = imp.find_module(self.title, commons.__path__)
		specifics = imp.load_module(self.title, specifics_info[0], specifics_info[1], specifics_info[2])
		print '> Module imported successfully: %s' % specifics

		bldr = builder.Builder(commons.params, specifics.params, self.title, test_name)
		bldr.build_cmd()
		self.job_dict = bldr.build_dict()

		return self.job_dict
