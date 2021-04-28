# -*- coding: utf-8 -*-
"""Module extension Database."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    """Extension SQLAlchemy Application Factory."""
    db.init_app(app)
    # Create database
    from flask_template.model import User  # noqa

    with app.app_context():
        try:
            db.create_all()
            db.session.commit()
        except:
            # Quando sobe a aplicação e já existe o banco criado
            ...
