import sqlite3
from ..database import get_db, close_db


class NodeRepository:
    @staticmethod
    def upload_form_data(filename, file_content):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO files (filename, content) VALUES (?, ?)",
                (filename, sqlite3.Binary(file_content))
            )
            
            db.commit()
        except sqlite3.Error as e:
            db.rollback()
            raise Exception(f"Database error: {str(e)}")
        finally:
            close_db()