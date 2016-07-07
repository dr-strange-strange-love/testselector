
class ParamHolder():
	def __init__(self):
		self.params = {
			'query_strings': {
				'master': 'nodes.inv_no = 220',
				'ts': 'nodes.inv_no = 768'
			},

			'prepares': {
				'master': [],
				'ts': [('image', 'win_10_en_x64', {'boot_arch': 'x86_64'})]
			}
		}

	def param_complement(self):
		# Complement code for self.params
		return self.params
