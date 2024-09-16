from flask import Blueprint, request, jsonify
from ..service.variableService import GlobalVariableService

global_variable_bp = Blueprint('global_variable', __name__, url_prefix='/api/global-variables')


@global_variable_bp.route('/<int:job_id>', methods=['GET'])
def get_global_variables(job_id):
    variables = GlobalVariableService.get_global_variables(job_id)
    return jsonify(variables)


@global_variable_bp.route('/<int:job_id>', methods=['POST'])
def create_global_variable(job_id):
    data = request.json
    variable_data = data.get('variable_data')
    if not variable_data:
        return jsonify({"error": "Variable data is required"}), 400
    new_id = GlobalVariableService.create_global_variable(job_id, variable_data)
    return jsonify({"id": new_id}), 201


@global_variable_bp.route('/<int:job_id>', methods=['PUT'])
def update_global_variable(job_id):
    data = request.json
    variable_data = data.get('variable_data')
    if not variable_data:
        return jsonify({"error": "Variable name and value are required"}), 400
    GlobalVariableService.update_global_variable(job_id, variable_data)
    return jsonify({"message": "Global variable updated successfully"}), 200


@global_variable_bp.route('/exist/<int:job_id>', methods=['GET'])
def check_existance(job_id):
    exists = GlobalVariableService.check_existance(job_id)
    return jsonify({"exists": exists})
