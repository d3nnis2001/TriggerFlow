from flask import Blueprint, request, jsonify
import subprocess


job_bp = Blueprint('job', __name__, url_prefix='/api/job')