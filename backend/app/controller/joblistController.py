from flask import Blueprint, request, jsonify
import subprocess
from ..service.joblistService import JoblistService

joblist_bp = Blueprint('joblist', __name__, url_prefix='/api/joblist')

@joblist_bp.route('/getAllJobs', methods=['POST'])
def getAllJobs():
    joblistServ = JoblistService()
    result = joblistServ.getAllJobs()
    return jsonify(result)
