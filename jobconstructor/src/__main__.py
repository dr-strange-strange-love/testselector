
""" This file is used to run jc/jobconstructor (src) package """

import argparse
import sys

from . import JobConstructor
from . import exceptions

def main():
	# Setting up command line argument parser
	parser = argparse.ArgumentParser(description='JobConstructor argument parser')
	parser.add_argument('--rootpath', action="store", dest="rootpath")
	parser.add_argument('--title', action="store", dest="title")
	# Reading arguments
	args = parser.parse_args(sys.argv[1:])

	# Getting job done
	cstr = JobConstructor(args.rootpath)
	job_params = 0
	try:
		job_params = cstr.get_job_by_title(args.title)
	except exceptions.JobConstructorException as e:
		sys.exit("Exiting with error: {0}".format(e))

	print '\n> Final job_params: %s' % job_params



if __name__ == "__main__":
	main()
