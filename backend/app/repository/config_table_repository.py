import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class ConfigTableRepository:
    @staticmethod
    def create(config_table: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO config_tables (job_id, table_name, table_data)
                VALUES (?, ?, ?)
            """, (config_table['job_id'], config_table['table_name'], config_table['table_data']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(config_table_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM config_tables WHERE id = ?", (config_table_id,))
            config_table = cursor.fetchone()
            return dict(config_table) if config_table else None
        finally:
            close_db()

    @staticmethod
    def get_all_by_job(job_id: int) -> List[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM config_tables WHERE job_id = ?", (job_id,))
            config_tables = cursor.fetchall()
            return [dict(config_table) for config_table in config_tables]
        finally:
            close_db()

    @staticmethod
    def update(config_table_id: int, config_table_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE config_tables
                SET job_id = ?, table_name = ?, table_data = ?
                WHERE id = ?
            """, (config_table_data['job_id'], config_table_data['table_name'],
                  config_table_data['table_data'], config_table_id))
            db.commit()
        finally:
            close_db()
        @staticmethod
        def delete(config_table_id: int) -> None:
            try:
                db = get_db()
                cursor = db.cursor()
                cursor.execute("DELETE FROM config_tables WHERE id = ?", (config_table_id,))
                db.commit()
            finally:
                close_db()