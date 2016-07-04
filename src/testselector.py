
import argparse
import imp
import os
import sys

import decoder

class TestSelector():
	def __init__(self):
		# resulting job dictionary
		job_dictionary = {}

	@staticmethod
	def main():
		# Setting up argument parser
		parser = argparse.ArgumentParser(description='TestSelector argument parser')
		parser.add_argument('--rootpath', action="store", dest="rootpath")
		parser.add_argument('--title', action="store", dest="title")
		# Reading arguments
		args = parser.parse_args(sys.argv[1:])

		# Creating decoder object
		dcdr = decoder.Decoder(args.rootpath, args.title)
		# Entering rootpath
		dcdr.set_dir_to_rootpath()
		# Getting required package name
		lcp = dcdr.get_package_name()

		# !ImportError
		# Importing required package (dynamically)
		pckg_info = imp.find_module(lcp, [args.rootpath])
		pckg = imp.load_module(lcp, pckg_info[0], pckg_info[1], pckg_info[2])
		print 'Package imported successfully: %s' % pckg

		# !ImportError, not too valid module import
		# Importing required module (dynamically)
		mod_info = imp.find_module(args.title, [os.path.join(args.rootpath, lcp)])
		mod = imp.load_module(args.title, mod_info[0], mod_info[1], mod_info[2])
		print 'Module imported successfully: %s' % mod

		print pckg.job_primary_parameters
		print mod.job_secondary_parameters



if __name__ == "__main__":
	TestSelector.main()
