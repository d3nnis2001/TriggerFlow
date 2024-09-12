import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class UserRepository:
    @staticmethod
    def create(user: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO users (first_name, last_name, email, password, role, firma)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user['first_name'], user['last_name'], user['email'], user['password'], user['role'], user['firma']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(user_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            return dict(user) if user else None
        finally:
            close_db()

    @staticmethod
    def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            return dict(user) if user else None
        finally:
            close_db()

    @staticmethod
    def update(user_id: int, user_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE users
                SET first_name = ?, last_name = ?, email = ?, password = ?, role = ?, firma = ?
                WHERE id = ?
            """, (user_data['first_name'], user_data['last_name'], user_data['email'],
                  user_data['password'], user_data['role'], user_data['firma'], user_id))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def delete(user_id: int) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            db.commit()
        finally:
            close_db()