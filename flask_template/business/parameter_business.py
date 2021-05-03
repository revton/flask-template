# -*- coding: utf-8 -*-
"""Module Parameter Business."""
from flask_template.extensions.database import db
from flask_template.model import Parameter


def create(parameter: Parameter):
    """Create new parameter."""
    db.session.add(parameter)
    try:
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        raise ex


def list():
    """List parameters"""
    return Parameter.query.all()
