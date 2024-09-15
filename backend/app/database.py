import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Function to create tables
def create_tables():
    db = get_db()
    cursor = db.cursor()

    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        firma TEXT NOT NULL
    )
    ''')

    # Jobs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        erstellungs_datum DATETIME DEFAULT CURRENT_TIMESTAMP,
        author_id INTEGER NOT NULL,
        firma TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY (author_id) REFERENCES users(id)
    )
    ''')

    # Config tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS config_tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        table_name TEXT NOT NULL,
        table_data TEXT NOT NULL,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    )
    ''')

    # Global variables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS global_variables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        variable_name TEXT NOT NULL,
        variable_value TEXT,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    )
    ''')

    # Nodes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        node_type TEXT NOT NULL,
        position_x REAL NOT NULL,
        position_y REAL NOT NULL,
        additional_info TEXT,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    )
    ''')

    # Schedules
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        schedule_type TEXT NOT NULL,
        start_time DATETIME,
        end_time DATETIME,
        recurrence_pattern TEXT,
        FOREIGN KEY (job_id) REFERENCES jobs(id)
    )
    ''')

    # Code snippets
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS code_snippets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        node_id INTEGER NOT NULL,
        snippet_name TEXT NOT NULL,
        snippet_content TEXT NOT NULL,
        FOREIGN KEY (node_id) REFERENCES nodes(id)
    )
    ''')

    # Edges
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS edges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        source_node_id INTEGER NOT NULL,
        target_node_id INTEGER NOT NULL,
        FOREIGN KEY (job_id) REFERENCES jobs(id),
        FOREIGN KEY (source_node_id) REFERENCES nodes(id),
        FOREIGN KEY (target_node_id) REFERENCES nodes(id)
    )
    ''')

    db.commit()

# Function to initialize the database
def initialize_database(app):
    with app.app_context():
        db = get_db()
        create_tables()
        close_db()

# Use this function in your Flask app initialization
def setup_database(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    initialize_database(app)