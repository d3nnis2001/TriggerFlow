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

    from .controller.joblistController import joblist_bp
    app.register_blueprint(joblist_bp)

    from .controller.nodeController import nodes_bp
    app.register_blueprint(nodes_bp)

    from .controller.configController import config_table_bp
    app.register_blueprint(config_table_bp)

    from .controller.jobController import job_bp
    app.register_blueprint(job_bp)

    return app
