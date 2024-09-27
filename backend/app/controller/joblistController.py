from flask import Blueprint, request, jsonify
from ..service.joblistService import JoblistService

joblist_bp = Blueprint('joblist', __name__, url_prefix='/api/joblist')

@joblist_bp.route('/getAllJobs', methods=['GET'])
def getAllJobs():
    joblistServ = JoblistService()
    result = joblistServ.getAllJobs()
    return jsonify(result)

@joblist_bp.route("/createJob", methods=["POST"])
def createJob():
    data = request.json
    result = JoblistService.createJob(data.get("name"), data.get("description"), data.get("comp"), data.get("image"))
    if result:
        return jsonify({
            "status": "success",
            "message": "Job created successfully",
            "job_id": result
        }), 201
    else:
        return jsonify({
            "status": "error",
            "message": "Failed to create job"
        }), 500
