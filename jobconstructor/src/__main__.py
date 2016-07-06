
""" This file is used to run jc (src) package """

import argparse
import sys

from . import constructor

def main():
	# Setting up command line argument parser
	parser = argparse.ArgumentParser(description='JobConstructor argument parser')
	parser.add_argument('--rootpath', action="store", dest="rootpath")
	parser.add_argument('--title', action="store", dest="title")
	# Reading arguments
	args = parser.parse_args(sys.argv[1:])

	# Getting job done
	cstr = constructor.Constructor(args.rootpath, args.title)
	print '\nFinal job_dict: %s' % cstr.construct()



if __name__ == "__main__":
	main()
