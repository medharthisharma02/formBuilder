# Application factory to initialize Flask formBuilder with configurations

from flask import Flask
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from config import Config
# from formBuilder.models import db
# from formBuilder.api.user_api import user_blueprint
# from formBuilder.api.document_api import document_blueprint
from formBuilder.api.home_api import home_blueprint
from formBuilder.handlers.errors import register_error_handlers

import logging
from logging.handlers import RotatingFileHandler
import os


def configure_logging(app):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/formbuilder.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Onboarded')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Talisman(app, content_security_policy=None)
    CSRFProtect(app)
    # db.init_app(app)
    configure_logging(app)
    register_error_handlers(app)
    # app.register_blueprint(document_blueprint, url_prefix='/api/documents')
    # app.register_blueprint(user_blueprint, url_prefix='/api/users')
    app.register_blueprint(home_blueprint)

    return app
