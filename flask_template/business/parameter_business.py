# -*- coding: utf-8 -*-
"""Module Parameter Business."""
from typing import List

from sqlalchemy.exc import NoResultFound

from flask_template.extensions.database import db
from flask_template.model import Parameter


def create(parameter: Parameter):
    """Create a new parameter."""
    db.session.add(parameter)
    try:
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        raise ex


def list_all() -> List[Parameter]:
    """List all parameters."""
    return Parameter.query.all()


def get_by_id(identifier: int) -> Parameter:
    """Get a parameter given its identifier."""
    return Parameter.query.get(identifier)


def update(identifier: int, parameter_new: dict) -> Parameter:
    """Update a parameter given its identifier."""
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


def delete_by_id(identifier: int) -> bool:
    """Delete a parameter given its identifier."""
    query = Parameter.query.filter(Parameter.id == identifier)
    if query.count() > 0:
        query.delete()
        return True
    raise NoResultFound("Parâmetro não encontrado.")
