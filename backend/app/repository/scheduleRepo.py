import sqlite3
from typing import List, Dict, Any, Optional
from ..database import get_db, close_db

class ScheduleRepository:
    @staticmethod
    def create(schedule: Dict[str, Any]) -> int:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO schedules (job_id, schedule_type, start_time, end_time, recurrence_pattern)
                VALUES (?, ?, ?, ?, ?)
            """, (schedule['job_id'], schedule['schedule_type'], schedule['start_time'],
                  schedule['end_time'], schedule['recurrence_pattern']))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_by_id(schedule_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM schedules WHERE id = ?", (schedule_id,))
            schedule = cursor.fetchone()
            return dict(schedule) if schedule else None
        finally:
            close_db()

    @staticmethod
    def get_by_job(job_id: int) -> Optional[Dict[str, Any]]:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM schedules WHERE job_id = ?", (job_id,))
            schedule = cursor.fetchone()
            return dict(schedule) if schedule else None
        finally:
            close_db()

    @staticmethod
    def update(schedule_id: int, schedule_data: Dict[str, Any]) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
                UPDATE schedules
                SET job_id = ?, schedule_type = ?, start_time = ?, end_time = ?, recurrence_pattern = ?
                WHERE id = ?
            """, (schedule_data['job_id'], schedule_data['schedule_type'], schedule_data['start_time'],
                  schedule_data['end_time'], schedule_data['recurrence_pattern'], schedule_id))
            db.commit()
        finally:
            close_db()

    @staticmethod
    def delete(schedule_id: int) -> None:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM schedules WHERE id = ?", (schedule_id,))
            db.commit()
        finally:
            close_db()