from flask import Flask
from config import Config
from .database import close_db
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    from .controller.editorController import editor_bp
    app.register_blueprint(editor_bp)

    from .controller.loginController import login_bp
    app.register_blueprint(login_bp)
    return app
