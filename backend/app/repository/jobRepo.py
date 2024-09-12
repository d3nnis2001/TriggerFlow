import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class JobRepository:
    @staticmethod
    def create(job: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO jobs (name, author_id, firma, description)
                VALUES (?, ?, ?, ?)
            """, (job['name'], job['author_id'], job['firma'], job['description']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(job_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
            job = cursor.fetchone()
            return dict(job) if job else None
        finally:
            close_db()

    @staticmethod
    def get_all_by_author(author_id: int) -> List[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM jobs WHERE author_id = ?", (author_id,))
            jobs = cursor.fetchall()
            return [dict(job) for job in jobs]
        finally:
            close_db()

    @staticmethod
    def update(job_id: int, job_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE jobs
                SET name = ?, author_id = ?, firma = ?, description = ?
                WHERE id = ?
            """, (job_data['name'], job_data['author_id'], job_data['firma'],
                  job_data['description'], job_id))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def delete(job_id: int) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
            db.commit()
        finally:
            close_db()