# -*- coding: utf-8 -*-
"""Module extension Admin."""
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_template.extensions.database import db
from flask_template.model import User

admin = Admin()


def init_app(app: Flask):
    """Flask-Admin Application Factory."""
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
