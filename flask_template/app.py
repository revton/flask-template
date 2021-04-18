# -*- coding: utf-8 -*-
from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    app = Flask(__name__)

    conf = FlaskDynaconf()
    conf.init_app(app, settings_file=["settings.toml", ".secrets.toml"])
    app.config.load_extensions()

    @app.route("/")
    def index():
        return f"<html><body>{app.config.APPLICATION_NAME}</body></html>"

    return app
