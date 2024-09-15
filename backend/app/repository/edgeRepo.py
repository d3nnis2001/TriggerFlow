import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class EdgeRepository:
    @staticmethod
    def create(edge: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO edges (job_id, source_node_id, target_node_id)
                VALUES (?, ?, ?)
            """, (edge['job_id'], edge['source_node_id'], edge['target_node_id']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(edge_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM edges WHERE id = ?", (edge_id,))
            edge = cursor.fetchone()
            return dict(edge) if edge else None
        finally:
            close_db()

    @staticmethod
    def get_all_by_job(job_id: int) -> List[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM edges WHERE job_id = ?", (job_id,))
            edges = cursor.fetchall()
            return [dict(edge) for edge in edges]
        finally:
            close_db()

    @staticmethod
    def update(edge_id: int, edge_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE edges
                SET job_id = ?, source_node_id = ?, target_node_id = ?
                WHERE id = ?
            """, (edge_data['job_id'], edge_data['source_node_id'],
                  edge_data['target_node_id'], edge_id))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def delete(edge_id: int) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM edges WHERE id = ?", (edge_id,))
            db.commit()
        finally:
            close_db()