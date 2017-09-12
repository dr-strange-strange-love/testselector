
from flask import Flask, jsonify
import os

from jobconstructor import JobConstructor
from jobconstructor import exceptions

application = Flask(__name__)
rootpath = "/hardcoded/rootpath"
jc = JobConstructor(rootpath)

if application.debug is not True:
	import logging
	from logging.handlers import RotatingFileHandler
	
	handler = RotatingFileHandler("jobconstructor_service.log", maxBytes=100000000, backupCount=5)
	handler.setLevel(logging.WARNING)
	formatter = logging.Formatter("%(asctime)s - %(module)s - %(lineno)d - %(levelname)s - %(message)s")
	handler.setFormatter(formatter)
	application.logger.addHandler(handler)



@application.route("/api/v1.0/job", methods=["GET"])
def get_info():
	if not os.path.exists(rootpath):
		application.logger.error("Warehouse [{0}] couldn't be located".format(rootpath))
		structure_dict = {"err_msg": "Warehouse [{0}] couldn't be located".format(rootpath)}
		return jsonify(structure_dict), 500

	# Getting list of all subdirectories (packages) in rootpath
	subdirs = [subdir for subdir in os.listdir(rootpath) if os.path.isdir(os.path.join(rootpath, subdir))]

	# constructing dictionary with hierarchy-related job info
	structure_dict = {}
	for subdir in subdirs:
		subdir_titles = [subdir_title.split('.')[0] for subdir_title \
			in os.listdir(os.path.join(rootpath, subdir)) if subdir_title.endswith(".py")]
		structure_dict[subdir] = subdir_titles

	return jsonify(structure_dict)

@application.route("/api/v1.0/job/<title>", methods=["GET"])
def get_json_by_title(title):
	try:
		job_dict = jc.get_job_by_title(title)
	except exceptions.JobConstructorException as e:
		application.logger.error(str(e))
		job_dict = {"err_msg": str(e)}
		return jsonify(job_dict), 404

	return jsonify(job_dict)

# This might be a hinderance
@application.errorhandler(404)
def page_not_found(e):
	application.logger.warning(str(e))
	return "Page not found", 404



if __name__ == "__main__":
	application.run(host='0.0.0.0')

