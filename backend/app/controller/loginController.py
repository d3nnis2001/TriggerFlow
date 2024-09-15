from flask import Blueprint, request, jsonify

from ..service.loginService import AuthService

login_bp = Blueprint('login', __name__, url_prefix='/api/login')

@login_bp.route('/checkLogin', methods=['POST'])
def check_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400

    try:
        success, message = AuthService.check_login(email, password)
        if success:
            return jsonify({'success': True, 'message': message}), 200
        else:
            return jsonify({'success': False, 'message': message}), 401
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'success': False, 'message': 'An error occurred'}), 500
