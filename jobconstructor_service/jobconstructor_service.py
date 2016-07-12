
from flask import Flask, jsonify
application = Flask(__name__)

import os

# jobconstructor here is src package
from jobconstructor import JobConstructor
from jobconstructor import exceptions

rootpath = '/home/amadeus/Documents/Field/testselector/job_warehouse'
jc = JobConstructor(rootpath)



@application.route("/api/v1.0/job", methods=['GET'])
def get_info():
	# Getting list of all subdirectories (packages) in rootpath
	subdirs = [subdir for subdir in os.listdir(rootpath) if os.path.isdir(os.path.join(rootpath, subdir))]

	# constructing dictionary with hierarchy-related job info
	structure_dict = {}
	for subdir in subdirs:
		subdir_titles = [subdir_title.split('.')[0] for subdir_title in os.listdir(os.path.join(rootpath, subdir)) if subdir_title.endswith(".py")]
		structure_dict[subdir] = subdir_titles

	return jsonify(structure_dict)

@application.route("/api/v1.0/job/<title>", methods=['GET'])
def get_json_by_title(title):
	try:
		job_dict = jc.get_job_by_title(title)
	except exceptions.JobConstructorException as e:
		job_dict = {'err_msg': str(e)}

	return jsonify(job_dict)
	


if __name__ == "__main__":
	application.run(host='0.0.0.0')

