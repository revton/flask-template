# -*- coding: utf-8 -*-
"""Module Parameter Business."""
from typing import List

from sqlalchemy.exc import NoResultFound

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


def list_all() -> List[Parameter]:
    """List parameters"""
    return Parameter.query.all()


def get_by_id(identifier: int) -> Parameter:
    return Parameter.query.get(identifier)


def update(identifier: int, parameter_new: dict) -> Parameter:
    query = Parameter.query.filter(Parameter.id == identifier)
    if query.count() > 0:
        try:
            query.update(parameter_new)
            db.session.commit()
            return query.first()
        except Exception as ex:
            db.session.rollback()
            raise ex
    raise NoResultFound("Parâmetro não encontrado.")
