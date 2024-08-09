import os

class Config:
    # Geheimer Schlüssel für die Sitzungssicherheit
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLite Datenbank-URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

    # Flask-SQLAlchemy Einstellungen
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail Einstellungen (falls Sie E-Mail-Funktionalität benötigen)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Anwendungsspezifische Einstellungen
    POSTS_PER_PAGE = 10

    # Flask-Debug-Toolbar (nur für Entwicklung)
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
