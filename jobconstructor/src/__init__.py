
from . import constructor

def get_job(rootpath, title):
	cstr = constructor.Constructor(rootpath, title)
	return cstr.construct()
