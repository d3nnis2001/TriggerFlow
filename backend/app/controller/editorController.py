from flask import Blueprint, request, jsonify
import subprocess

editor_bp = Blueprint('editor', __name__, url_prefix='/api/editor')

@editor_bp.route('/runCode', methods=['POST'])
def run_code():
    code = request.form.get('code')
    line_count = request.form.get('linecount')

    # Hier würden Sie den Code ausführen und das Ergebnis zurückgeben
    output = execute_code(code)

    return jsonify({'output': output})

@editor_bp.route('/refreshCode', methods=['POST'])
def refresh_code():
    code = request.form.get('code')
    line_count = request.form.get('linecount')
    curr_col = request.form.get('currCol')

    # Hier würden Sie den Code erneut ausführen und das aktualisierte Ergebnis zurückgeben
    output = execute_code(code, curr_col)

    return jsonify({'output': output})

def execute_code(code, curr_col=None):
    # Hier würden Sie den Code ausführen und das Ergebnis zurückgeben
    try:
        # Beispiel: Führen Sie den Python-Code aus und geben Sie die Ausgabe zurück
        result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Fehler beim Ausführen des Codes: {e}"