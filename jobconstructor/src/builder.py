
class Builder(object):
	def __init__(self, common_params, specific_params, test_name, title):
		self.common_params = common_params
		self.specific_params = specific_params
		self.test_name = test_name
		self.title = title

		self.cmd_line = ('python ' + self.test_name + '/00main.py execute -- '
		'--extra-param priority={priority} '
		'--extra-param assignee={assignee} '
		'--extra-param prefixes={prefixes} '
		'--extra-param components={components} '
		'--extra-param fixversions={fixversions} '
		'--title {title} '
		'{base_cmd_line} '
		'{spec_cmd_line}')

		self.job_dict = {
			'priority': '',
			'assigne': '',
			'prefixes': '',
			'components': '',
			'fixversions': '',
			'title': '',
			'base_cmd_line': '',
			'spec_cmd_line': '',
		}

	def build_dict(self):
		self.job_dict['test_name'] = self.test_name
		self.job_dict['title'] = self.title
		self.job_dict['cmd_line'] = self.cmd_line
		self.job_dict.update(self.common_params)
		self.job_dict.update(self.specific_params)

		return self.job_dict
