from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class GlobalVariableRepository:
    @staticmethod
    def create(global_variable: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO global_variables (job_id, variable_data)
                VALUES (?, ?, ?)
            """, (global_variable['job_id'], global_variable['variable_data']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_job_id(job_id: int) -> List[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM global_variables WHERE job_id = ?", (job_id,))
            variables = cursor.fetchall()
            return [dict(variable) for variable in variables]
        finally:
            close_db()

    @staticmethod
    def update(job_id: int, variable_data: str) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE global_variables
                SET variable_data = ?
                WHERE job_id = ?
            """, (job_id, variable_data))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def numvariables(job_id: int) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM global_variables WHERE job_id = ?", (job_id,))
            count = cursor.fetchone()[0]
            return count
        finally:
            close_db()
