
class Builder():
	def __init__(self, common_params, specific_params, title, test_name):
		self.common_params = common_params
		self.specific_params = specific_params
		self.title = title
		self.test_name = test_name
		self.cmd_line = ''
		self.jod_dict = {}

	def build_cmd(self):
		self.cmd_line = \
		'python ' + self.test_name + '/00main.py execute -- ' \
		'--ts {ts} --build {build} --validation ' \
		'--url-manager {url_manager} ' \
		'--portal {portal} ' \
		'--extra-param priority={priority} ' \
		'--extra-param assignee={assignee} ' \
		'--extra-param prefixes={prefixes} ' \
		'--extra-param components={components} ' \
		'--extra-param fixversions={fixversions} ' \
		'--title {title}'

	def build_dict(self):
		self.jod_dict['test_name'] = self.test_name
		self.jod_dict['title'] = self.title
		self.jod_dict.update(self.common_params)
		self.jod_dict.update(self.specific_params)
		self.jod_dict['cmd_line'] = self.cmd_line

		return self.jod_dict
