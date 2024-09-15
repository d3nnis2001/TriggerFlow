import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class NodeRepository:
    @staticmethod
    def create(node: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO nodes (job_id, node_type, position_x, position_y, additional_info)
                VALUES (?, ?, ?, ?, ?)
            """, (node['job_id'], node['node_type'], node['position_x'], node['position_y'], node['additional_info']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(node_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM nodes WHERE id = ?", (node_id,))
            node = cursor.fetchone()
            return dict(node) if node else None
        finally:
            close_db()

    @staticmethod
    def get_all_by_job(job_id: int) -> List[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM nodes WHERE job_id = ?", (job_id,))
            nodes = cursor.fetchall()
            return [dict(node) for node in nodes]
        finally:
            close_db()

    @staticmethod
    def update(node_id: int, node_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE nodes
                SET job_id = ?, node_type = ?, position_x = ?, position_y = ?, additional_info = ?
                WHERE id = ?
            """, (node_data['job_id'], node_data['node_type'], node_data['position_x'],
                  node_data['position_y'], node_data['additional_info'], node_id))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def delete(node_id: int) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM nodes WHERE id = ?", (node_id,))
            db.commit()
        finally:
            close_db()