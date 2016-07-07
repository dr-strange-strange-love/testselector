
class ParamHolder():
	def __init__(self):
		self.params = {
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

	def param_complement(self):
		# Complement code for self.params
		return self.params
