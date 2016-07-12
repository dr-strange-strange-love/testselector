
import os
import unittest

from ..src import JobConstructor
from ..src import builder
from ..src import decoder

class BuilderTestCase(unittest.TestCase):
	def setUp(self):
		self.commons_dict = {
			'build': '3.5.0-31804',
			'priority': 'Blocker',

			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},

			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			},

			'base_cmd_line': '--ts {ts} --build {build} --validation'
		}

	def tearDown(self):
		pass

	def test_build_dict(self):
		specifics_dict = {
			'build': '3.5.0-31805',
			'priority': '',
			'components': 'QA_auto',
			'fixversions': '',
			'spec_cmd_line': '--portal {portal}'
		}

		expected_dict = {
			'test_name': 'vzt-pgov',

			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title} ' \
				'--base-cmd-line {base_cmd_line} ' \
				'--spec-cmd-line {spec_cmd_line}',

			'priority': '',
			'assigne': '',
			'prefixes': '',
			'components': 'QA_auto',
			'fixversions': '',
			'title': 'vzt-pgov-win10x32-el_capitan-up',
			'base_cmd_line': '--ts {ts} --build {build} --validation',
			'spec_cmd_line': '--portal {portal}',

			'build': '3.5.0-31805',

			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},

			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			}
		}

		bldr = builder.Builder(self.commons_dict, specifics_dict, 'vzt-pgov', 'vzt-pgov-win10x32-el_capitan-up')
		built_dict = bldr.build_dict()
		self.assertEqual(cmp(built_dict, expected_dict), 0)

	def test_build_dict_2(self):
		specifics_dict = {}

		expected_dict = {
			'test_name': 'vzt-pgov',

			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title} ' \
				'--base-cmd-line {base_cmd_line} ' \
				'--spec-cmd-line {spec_cmd_line}',

			'priority': 'Blocker',
			'assigne': '',
			'prefixes': '',
			'components': '',
			'fixversions': '',
			'title': 'vzt-pgov-fedora-23-x86_64-yosemite-up',
			'base_cmd_line': '--ts {ts} --build {build} --validation',
			'spec_cmd_line': '',

			'build': '3.5.0-31804',

			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},

			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			}
		}

		bldr = builder.Builder(self.commons_dict, specifics_dict, 'vzt-pgov', 'vzt-pgov-fedora-23-x86_64-yosemite-up')
		built_dict = bldr.build_dict()
		self.assertEqual(cmp(built_dict, expected_dict), 0)



class DecoderTestCase(unittest.TestCase):
	def setUp(self):
			self.rootpath = os.path.abspath('job_warehouse')

	def tearDown(self):
		pass

	def test_get_package_name(self):
		title = 'vzt-pgov-fedora-23-x86_64-yosemite-up'
		expected_package_name = 'vzt-pgov'

		dcdr = decoder.Decoder(self.rootpath, title)
		self.assertEqual(dcdr.get_package_name(), expected_package_name)

	def test_get_package_name_2(self):
		title = 'vzt-pgov-stress_win10x32-yosemite-bottom'
		expected_package_name = 'vzt-pgov-stress'

		dcdr = decoder.Decoder(self.rootpath, title)
		self.assertEqual(dcdr.get_package_name(), expected_package_name)



class JobConstructorTestCase(unittest.TestCase):
	def setUp(self):
		self.rootpath = os.path.abspath('job_warehouse')

	def tearDown(self):
		pass

	def test_get_job_by_title(self):
		title = 'vzt-pgov-win10x32-el_capitan-up'
		expected_dict = {
			'test_name': 'vzt-pgov',

			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title} ' \
				'--base-cmd-line {base_cmd_line} ' \
				'--spec-cmd-line {spec_cmd_line}',

			'priority': '',
			'assigne': '',
			'prefixes': '',
			'components': 'QA_auto',
			'fixversions': '',
			'title': 'vzt-pgov-win10x32-el_capitan-up',
			'base_cmd_line': '--ts {ts} --build {build} --validation',
			'spec_cmd_line': '--portal {portal}',

			'build': '3.5.0-31805',

			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},

			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			}
		}

		jc = JobConstructor(self.rootpath)
		built_dict = jc.get_job_by_title(title)
		self.assertEqual(cmp(built_dict, expected_dict), 0)



if __name__ == "__main__":
	unittest.main()
