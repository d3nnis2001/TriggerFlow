import sqlite3
from ..database import get_db, close_db

class JoblistRepository:
    @staticmethod
    def get_all_jobs():
        try:
            db = get_db()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute("SELECT * FROM jobs")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            close_db()

    @staticmethod
    def create(name, image, comp, desc) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO jobs (name, image, firma, description)
                VALUES (?, ?, ?, ?)
            """, (name, image, comp, desc))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()