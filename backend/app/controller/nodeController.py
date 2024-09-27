from flask import Blueprint, request, jsonify
from ..service.nodeService import NodeService

nodes_bp = Blueprint('nodes', __name__, url_prefix='/api/nodes')

@nodes_bp.route('/uploadFiles', methods=['POST'])
def upload_files():
    files = request.files.getlist('demo[]')
    
    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # NodeService.upload_data(files)
        return jsonify({"message": "Files uploaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500