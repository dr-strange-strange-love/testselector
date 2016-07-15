
import imp

from . import builder
from . import decoder
from . import exceptions

class JobConstructor(object):
	def __init__(self, rootpath):
		self.rootpath = rootpath

	def get_job_by_title(self, title):
		dcdr = decoder.Decoder(self.rootpath, title)		
		test_name = dcdr.get_package_name() # Getting required package name

		# Importing required package
		try:
			commons_info = imp.find_module(test_name, [self.rootpath])
			commons = imp.load_module(test_name, commons_info[0], commons_info[1], commons_info[2])
		except ImportError:
			raise exceptions.JobConstructorException("Package [{0}] couldn't be imported".format(test_name))
		cms = commons.ParamHolder()

		# Importing required module
		try:
			specifics_info = imp.find_module(title, commons.__path__)
			specifics = imp.load_module(title, specifics_info[0], specifics_info[1], specifics_info[2])
		except ImportError:
			raise exceptions.JobConstructorException("Module [{0}] couldn't be imported".format(title))
		sps = specifics.ParamHolder()

		bldr = builder.Builder(cms.param_complement(), sps.param_complement(), test_name, title)

		return bldr.build_dict()
