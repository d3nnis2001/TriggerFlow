from flask import Blueprint, request, jsonify
from ..service.variableService import GlobalVariableService
from typing import List, Dict

global_variable_bp = Blueprint('global_variable', __name__, url_prefix='/api/global-variables')


@global_variable_bp.route('/<int:job_id>', methods=['GET'])
def get_global_variables(job_id: int):
    variables = GlobalVariableService.get_global_variables(job_id)
    return jsonify(variables)


@global_variable_bp.route('/<int:job_id>', methods=['POST'])
def create_global_variable(job_id: int):
    data = request.json
    variable_data: List[Dict[str, str]] = data.get('variable_data')
    if not variable_data:
        return jsonify({"error": "Variable data is required"}), 400
    new_id = GlobalVariableService.create_global_variable(job_id, variable_data)
    return jsonify({"id": new_id}), 201


@global_variable_bp.route('/<int:job_id>', methods=['PUT'])
def update_global_variable(job_id: int):
    data = request.json
    variable_data: List[Dict[str, str]] = data.get('variable_data')
    if not variable_data:
        return jsonify({"error": "Variable data is required"}), 400
    GlobalVariableService.update_global_variable(job_id, variable_data)
    return jsonify({"message": "Global variables updated successfully"}), 200


@global_variable_bp.route('/exist/<int:job_id>', methods=['GET'])
def check_existance(job_id: int):
    exists = GlobalVariableService.check_existance(job_id)
    return jsonify({"exists": exists})