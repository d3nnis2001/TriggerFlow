from ..repository.userRepo import UserRepository

class AuthService:
    @staticmethod
    def check_login(email, password):
        user = UserRepository.get_user_by_email(email)
        if user is None:
            return False, 'Email does not exist'
        if user['password'] == password:  # TODO: Use check_password_hash here
            return True, 'Login successful'
        return False, 'Invalid credentials'
