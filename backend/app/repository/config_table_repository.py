import json
from ..database import get_db, close_db

class ConfigTableRepository:
    @staticmethod
    def create_table(name, description, structure, data):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('''
            INSERT INTO configuration_tables (name, description, structure, data)
            VALUES (?, ?, ?, ?)
            ''', (name, description, json.dumps(structure), json.dumps(data)))
            db.commit()
            return cursor.lastrowid
        finally:
            close_db()

    @staticmethod
    def get_all_tables():
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('SELECT * FROM configuration_tables')
            tables = cursor.fetchall()
            return [dict(table) for table in tables]
        finally:
            close_db()

    @staticmethod
    def get_table_by_id(table_id):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('SELECT * FROM configuration_tables WHERE id = ?', (table_id,))
            table = cursor.fetchone()
            if table:
                table = dict(table)
                table['structure'] = json.loads(table['structure'])
                table['data'] = json.loads(table['data'])
            return table
        finally:
            close_db()

    @staticmethod
    def update_table(table_id, name, description, structure, data):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('''
            UPDATE configuration_tables
            SET name = ?, description = ?, structure = ?, data = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            ''', (name, description, json.dumps(structure), json.dumps(data), table_id))
            db.commit()
            return cursor.rowcount > 0
        finally:
            close_db()

    @staticmethod
    def delete_table(table_id):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('DELETE FROM configuration_tables WHERE id = ?', (table_id,))
            db.commit()
            return cursor.rowcount > 0
        finally:
            close_db()