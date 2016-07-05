
import sys
import unittest

from ..src import builder
from ..src import decoder
from ..src import constructor

class BuilderTestCase(unittest.TestCase):
	def setUp(self):
		self.expected_cmd_line = \
		'python vzt-pgov/00main.py execute -- ' \
		'--ts {ts} --build {build} --validation ' \
		'--url-manager {url_manager} ' \
		'--portal {portal} ' \
		'--extra-param priority={priority} ' \
		'--extra-param assignee={assignee} ' \
		'--extra-param prefixes={prefixes} ' \
		'--extra-param components={components} ' \
		'--extra-param fixversions={fixversions} ' \
		'--title {title}'

		self.expected_cmd_line_2 = \
		'python vzt-hdd-stress/00main.py execute -- ' \
		'--ts {ts} --build {build} --validation ' \
		'--url-manager {url_manager} ' \
		'--portal {portal} ' \
		'--extra-param priority={priority} ' \
		'--extra-param assignee={assignee} ' \
		'--extra-param prefixes={prefixes} ' \
		'--extra-param components={components} ' \
		'--extra-param fixversions={fixversions} ' \
		'--title {title}'

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
			}
		}

		self.specifics_dict = {
			'build': '3.5.0-31805',
			'priority': '',
			'components': 'QA_auto',
			'fixversions': ''
		}

		self.specifics_dict_2 = {}

		self.expected_dict = {
			'priority': '',
			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},
			'build': '3.5.0-31805',
			'components': 'QA_auto',
			'title': 'vzt-pgov-win10x32-el_capitan-up',
			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			},
			'test_name': 'vzt-pgov',
			'fixversions': '',
			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--ts {ts} --build {build} --validation ' \
				'--url-manager {url_manager} ' \
				'--portal {portal} ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title}'
		}

		self.expected_dict_2 = {
			'priority': 'Blocker',
			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},
			'build': '3.5.0-31804',
			'title': 'vzt-pgov-fedora-23-x86_64-yosemite-up',
			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			},
			'test_name': 'vzt-pgov',
			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--ts {ts} --build {build} --validation ' \
				'--url-manager {url_manager} ' \
				'--portal {portal} ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title}'
		}

	def tearDown(self):
		pass

	def test_build_cmd(self):
		bldr = builder.Builder({}, {}, '', 'vzt-pgov')
		bldr.build_cmd()
		self.assertEqual(bldr.cmd_line, self.expected_cmd_line)

	def test_build_cmd_2(self):
		bldr = builder.Builder({}, {}, '', 'vzt-hdd-stress')
		bldr.build_cmd()
		self.assertEqual(bldr.cmd_line, self.expected_cmd_line_2)

	def test_build_dict(self):
		bldr = builder.Builder(self.commons_dict, self.specifics_dict, 'vzt-pgov-win10x32-el_capitan-up', 'vzt-pgov')
		bldr.cmd_line = \
		'python vzt-pgov/00main.py execute -- ' \
		'--ts {ts} --build {build} --validation ' \
		'--url-manager {url_manager} ' \
		'--portal {portal} ' \
		'--extra-param priority={priority} ' \
		'--extra-param assignee={assignee} ' \
		'--extra-param prefixes={prefixes} ' \
		'--extra-param components={components} ' \
		'--extra-param fixversions={fixversions} ' \
		'--title {title}'
		built_dict = bldr.build_dict()
		self.assertEqual(cmp(built_dict, self.expected_dict), 0)

	def test_build_dict_2(self):
		bldr = builder.Builder(self.commons_dict, self.specifics_dict_2, 'vzt-pgov-fedora-23-x86_64-yosemite-up', 'vzt-pgov')
		bldr.cmd_line = \
		'python vzt-pgov/00main.py execute -- ' \
		'--ts {ts} --build {build} --validation ' \
		'--url-manager {url_manager} ' \
		'--portal {portal} ' \
		'--extra-param priority={priority} ' \
		'--extra-param assignee={assignee} ' \
		'--extra-param prefixes={prefixes} ' \
		'--extra-param components={components} ' \
		'--extra-param fixversions={fixversions} ' \
		'--title {title}'
		built_dict = bldr.build_dict()
		self.assertEqual(cmp(built_dict, self.expected_dict_2), 0)



class DecoderTestCase(unittest.TestCase):
	def setUp(self):
		self.rootpath = 'C:\\Users\\Amadeus\\Desktop\\Field\\testselector\\warehouse'
		self.title = 'vzt-pgov-fedora-23-x86_64-yosemite-up'
		self.expected_package_name = 'vzt-pgov'

	def tearDown(self):
		pass

	def test_check_rootpath(self):
		dcdr = decoder.Decoder(self.rootpath, '')
		self.assertEqual(dcdr.check_rootpath(), 1)

	def test_get_package_name(self):
		dcdr = decoder.Decoder(self.rootpath, self.title)
		self.assertEqual(dcdr.get_package_name(), self.expected_package_name)

class ConstructorTestCase(unittest.TestCase):
	def setUp(self):
		self.rootpath = 'C:\\Users\\Amadeus\\Desktop\\Field\\testselector\\warehouse'
		self.title = 'vzt-pgov-win10x32-el_capitan-up'

		self.expected_dict = {
			'priority': '',
			'query_strings': {
				'master': 'nodes.inv_no = 240',
				'ts': 'nodes.inv_no = 368'
			},
			'build': '3.5.0-31805',
			'components': 'QA_auto',
			'title': 'vzt-pgov-win10x32-el_capitan-up',
			'prepares': {
				'master': [],
				'ts': [('image', 'win_7_sp1_en_x64', {'edition': 'Windows 7 ULTIMATE', 'boot_arch': 'x86_64'})]
			},
			'test_name': 'vzt-pgov',
			'fixversions': '',
			'cmd_line': 'python vzt-pgov/00main.py execute -- ' \
				'--ts {ts} --build {build} --validation ' \
				'--url-manager {url_manager} ' \
				'--portal {portal} ' \
				'--extra-param priority={priority} ' \
				'--extra-param assignee={assignee} ' \
				'--extra-param prefixes={prefixes} ' \
				'--extra-param components={components} ' \
				'--extra-param fixversions={fixversions} ' \
				'--title {title}'
		}

	def tearDown(self):
		pass

	def test_construct(self):
		cstr = constructor.Constructor(self.rootpath, self.title)
		built_dict = cstr.construct()
		self.assertEqual(cmp(built_dict, self.expected_dict), 0)



if __name__ == "__main__":
	unittest.main()
