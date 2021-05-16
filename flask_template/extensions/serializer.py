# -*- coding: utf-8 -*-
"""Module extension Serializer."""
from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_app(app):
    """Extension Marshmallow Application Factory."""
    ma.init_app(app)
