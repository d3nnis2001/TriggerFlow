from flask import Blueprint, request, jsonify
from ..service.configService import ConfigTableService

config_table_bp = Blueprint('config_table', __name__, url_prefix='/api/config-tables')


@config_table_bp.route('/<int:table_id>', methods=['POST'])
def create_table(table_id):
    data = request.json
    resp = ConfigTableService.create_table(
        table_id, data['job_id'], data['table_name'], data['table_data']
    )
    return jsonify(resp), 201


@config_table_bp.route('/job/<int:job_id>', methods=['GET'])
def get_all_tables_by_job(job_id):
    tables = ConfigTableService.get_all_tables_by_job(job_id)
    return jsonify(tables)


@config_table_bp.route('/<int:table_id>', methods=['GET'])
def get_table(table_id):
    table = ConfigTableService.get_table_by_id(table_id)
    if table:
        return jsonify(table)
    return jsonify({"error": "Table not found"}), 404


@config_table_bp.route('/<int:table_id>', methods=['PUT'])
def update_table(table_id):
    data = request.json
    success = ConfigTableService.update_table(
        table_id, data['job_id'], data['table_name'], data['table_data']
    )
    return jsonify({"message": "Table updated successfully"}), 200


@config_table_bp.route('/<int:table_id>', methods=['DELETE'])
def delete_table(table_id):
    ConfigTableService.delete_table(table_id)
    return jsonify({"message": "Table deleted successfully"}), 200
