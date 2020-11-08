from flask import Flask

from logging.handlers import WatchedFileHandler
import logging

from project import models
from project.views import main_views
from . import config

def create_app():
    # 플라스크 앱 
    app = Flask(__name__)

    app.config.from_object(config) 

    # @app.before_first_request
    handler = WatchedFileHandler("/home/ato/lecturedocapp.log")
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    # Blueprint
    app.register_blueprint(main_views.bp)

    return app 