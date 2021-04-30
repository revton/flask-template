# -*- coding: utf-8 -*-
"""Module extension Database."""
from flask import Flask
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def init_app(app: Flask):
    """Extension SQLAlchemy and Migrate Application Factory."""
    # Import database model
    from flask_template.model import Parameter, User  # noqa

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    # Create database
    with app.app_context():
        upgrade()
