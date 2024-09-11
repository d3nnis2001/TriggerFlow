from flask import Blueprint, request, jsonify
from ..service.config_table_service import ConfigTableService

config_table_bp = Blueprint('config_table', __name__, url_prefix='/api/config-tables')

@config_table_bp.route('', methods=['POST'])
def create_table():
    data = request.json
    table_id = ConfigTableService.create_table(
        data['name'], data['description'], data['columns'], data['data']
    )
    return jsonify({"id": table_id}), 201

@config_table_bp.route('', methods=['GET'])
def get_all_tables():
    tables = ConfigTableService.get_all_tables()
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
        table_id, data['name'], data['description'], data['columns'], data['data']
    )
    if success:
        return jsonify({"message": "Table updated successfully"})
    return jsonify({"error": "Table not found"}), 404

@config_table_bp.route('/<int:table_id>', methods=['DELETE'])
def delete_table(table_id):
    success = ConfigTableService.delete_table(table_id)
    if success:
        return jsonify({"message": "Table deleted successfully"})
    return jsonify({"error": "Table not found"}), 404