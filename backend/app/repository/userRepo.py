import sqlite3
from ..database import get_db, close_db

class UserRepository:
    @staticmethod
    def get_user_by_email(email):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
            user = cursor.fetchone()
            return user
        finally:
            close_db()
