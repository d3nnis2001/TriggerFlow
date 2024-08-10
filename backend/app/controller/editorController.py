from flask import Blueprint, request, jsonify
import subprocess

editor_bp = Blueprint('editor', __name__, url_prefix='/api/editor')

@editor_bp.route('/runCode', methods=['POST'])
def run_code():
    print("HELLO")
    code = request.form.get('code')
    line_count = request.form.get('linecount')
    output = execute_code(code)

    return jsonify({'output': output})

@editor_bp.route('/refreshCode', methods=['POST'])
def refresh_code():
    code = request.form.get('code')
    line_count = request.form.get('linecount')
    curr_col = request.form.get('currCol')

    output = execute_code(code, curr_col)

    return jsonify({'output': output})


def execute_code(code, curr_col=None):
    try:
        result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Fehler beim Ausführen des Codes: {e}"
