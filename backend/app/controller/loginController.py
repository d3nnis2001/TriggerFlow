from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
import sqlite3

login_bp = Blueprint('editor', __name__, url_prefix='/api/login')

login_bp.route('checkLogin', methods=['POST'])
def check_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400

    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result:
            stored_password_hash = result[0]
            if check_password_hash(stored_password_hash, password):
                return jsonify({'success': True, 'message': 'Login successful'}), 200
            else:
                return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
        else:
            return jsonify({'success': False, 'message': 'User not found'}), 404

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return jsonify({'success': False, 'message': 'An error occurred'}), 500

    finally:
        conn.close()
