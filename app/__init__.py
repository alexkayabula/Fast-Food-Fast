from flask import Flask
from flask_cors import CORS
from config import app_config
from app.database.database import *
from app.error_handler import *


def create_app(config_name):
    """
        Creates the application and registers the blueprints
        with the application
    """
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config.from_object(app_config[config_name])

    from app.auth.views import AUTH_BLUEPRINT
    from app.menu.views import MENU_BLUEPRINT
    from app.order.views import ORDER_BLUEPRINT
    app.register_blueprint(AUTH_BLUEPRINT)
    app.register_blueprint(MENU_BLUEPRINT)
    app.register_blueprint(ORDER_BLUEPRINT)
    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(405, method_not_allowed)

    return app