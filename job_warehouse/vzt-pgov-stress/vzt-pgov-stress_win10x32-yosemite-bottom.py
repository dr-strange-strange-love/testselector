
class ParamHolder():
	def __init__(self):
		self.params = {
			'build': '3.5.0-31806',
			'priority': '',
			'components': 'QA_auto',
			'fixversions': '',
			
			'nodes_attribute': {
				'master': {'force_redeploy': 'False', 'leave_dirty': 'False'},
				'ts': {'force_redeploy': 'True'}
			}
		}

	def param_complement(self):
		# Complement code for self.params
		return self.params
