import sqlite3
from ..database import get_db, close_db

class JoblistRepository:
    @staticmethod
    def get_all_jobs():
        try:
            db = get_db()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute("SELECT * FROM job")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            close_db()

    @staticmethod
    def get_jobs_comp(company):
        try:
            db = get_db()
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute("SELECT * FROM job WHERE firma = ?", (company,))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            close_db()
