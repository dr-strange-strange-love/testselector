
""" This is the interface for jc (src) package """

from . import constructor

def get_job(rootpath, title):
	cstr = constructor.Constructor(rootpath, title)
	res = cstr.construct() # res either receives constructed job dictionary or error code

	return res
