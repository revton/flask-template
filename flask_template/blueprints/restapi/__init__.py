# -*- coding: utf-8 -*-
""" Module RestAPI."""
from flask import Blueprint
from flask_restx import Api

from flask_template.blueprints.restapi.parameter_namespace import ns_parameter

blueprint_api = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api()


def init_app(app):
    api.init_app(blueprint_api)
    api.add_namespace(ns_parameter)
    app.register_blueprint(blueprint_api)

    # @api.errorhandler
    # def default_error_handler(error):
    #     """Default error handler."""
    #     return {"message": str(error)}, getattr(error, "status_code", 500)
