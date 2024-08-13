# database.py

import sqlite3
from flask import g

DATABASE = 'triggerflow.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    db = g.pop('_database', None)
    if db is not None:
        db.close()

def init_db():
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        ''')
        db.commit()

# Fügen Sie diese Funktion hinzu, um einen Testbenutzer zu erstellen
def create_test_user(email, password):
    with get_db() as db:
        cursor = db.cursor()
        cursor.execute('INSERT OR REPLACE INTO user (email, password) VALUES (?, ?)', (email, password))
        db.commit()
