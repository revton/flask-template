# -*- coding: utf-8 -*-
"""Module db Model."""
from flask_template.extensions.database import db


class User(db.Model):
    """Class User."""

    ___tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"


class Parameter(db.Model):
    """Class Parameter."""

    ___tablename__ = "parameters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    value = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Parameter(name={self.name}, value={self.value})>"
