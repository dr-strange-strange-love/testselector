
"""
!!!
It is ADVISABLE not to use/import this (jobconstructor) package in external modules (intended usage is for testing).
Use/import src package instead (rename it to your liking and remove __main__.py module).
For safety reasons jobconstructor provides interface to src.
!!!
"""

from .src import JobConstructor as JC
'''
одного этого импорта будет достаточно, оборачивать не нужно
'''

class JobConstructor():
	def __init__(self, rootpath):
		jc = JC(self.rootpath)

	def get_job_by_title(self, title):
		return jc.get_job_by_title(title)
