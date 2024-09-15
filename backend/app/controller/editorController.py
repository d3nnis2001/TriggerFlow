from flask import Blueprint, request, jsonify
import subprocess
from ..service.editorService import EditorService

editor_bp = Blueprint('editor', __name__, url_prefix='/api/editor')

@editor_bp.route('/runCode', methods=['POST'])
def run_code():
    code = request.form.get('code')
    line_count = request.form.get('linecount')
    curr_col = request.form.get('currCol')
    tableName = request.form.get('tableName')
    # TODO: tablename anstatt BTCUSDT3600 nehmen weil Hardcoded hier
    editServ = EditorService("BTCUSDT3600")
    editServ.is_code_safe(code)
    return editServ.run_code(code, curr_col)

@editor_bp.route('/refreshCode', methods=['POST'])
def refresh_code():
    code = request.form.get('code')
    line_count = request.form.get('linecount')
    curr_col = request.form.get('currCol')

    return jsonify({'output'})
