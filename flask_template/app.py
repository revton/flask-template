# -*- coding: utf-8 -*-
import datetime

from dynaconf import FlaskDynaconf
from flask import Flask


def create_app():
    app = Flask(__name__)

    conf = FlaskDynaconf()
    conf.init_app(app, settings_file=["settings.toml", ".secrets.toml"])
    app.config.load_extensions()

    configure_logging(app)
    configure_request(app)

    @app.route("/")
    def index():
        app.logger.info("INFO")
        app.logger.error("ERROR")
        app.logger.warning("WARNING")
        return f"<html><body>{app.config.APPLICATION_NAME}</body></html>"

    return app


def configure_logging(app: Flask):
    """
    Definir as configurações de logging da aplicação
    :param app:
    """
    import logging
    import os
    from logging.config import dictConfig
    from logging.handlers import RotatingFileHandler

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(name)s][%(asctime)s] %(levelname)s "
                              "in %(module)s.%(funcName)s[Line:%(lineno)d]: "
                              "%(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    if not os.path.exists(app.config["LOG_FOLDER"]):
        os.makedirs(app.config["LOG_FOLDER"], exist_ok=True)

    log_filepath = os.path.join(
        app.config["LOG_FOLDER"], f"{datetime.datetime.now().date()}.log"
    )

    info_file_handler = RotatingFileHandler(
        log_filepath, maxBytes=100000, backupCount=10
    )
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(
        logging.Formatter(
            "[%(name)s][%(asctime)s] %(levelname)s "
            "in %(module)s.%(funcName)s[Line:%(lineno)d]: "
            "%(message)s"
        )
    )
    app.logger.addHandler(info_file_handler)


def configure_request(app: Flask):
    from flask import request

    @app.before_request
    def log_before_request():
        """
        Loga dados antes de todas requisições
        """
        app.logger.info(
            "\t".join(
                [
                    datetime.datetime.today().ctime(),
                    request.remote_addr,
                    request.method,
                    request.url,
                    ", ".join([": ".join(x) for x in request.headers]),
                ]
            )
        )

    @app.after_request
    def log_after_request(response):
        """
        Loga dados depois de todas requisições com sucesso
        """
        if response.status_code == 200:
            app.logger.info(
                "\t".join(
                    [
                        datetime.datetime.today().ctime(),
                        str(response.status_code),
                        ", ".join([": ".join(x) for x in response.headers]),
                    ]
                )
            )
        return response
