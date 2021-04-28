# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.exc import IntegrityError

from flask_template.model import User


def test_admin_user_new(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user = User(name="Revton", email="revtonbr@gmail.com")
    db.session.add(user)
    db.session.commit()
    assert "<User(name=Revton, email=revtonbr@gmail.com)>" == repr(
        User.query.filter_by(name="Revton").first()
    )


def test_admin_user_new_name_unique_validation(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user = User(name="Revton", email="revtonbr@gmail.com")
    db.session.add(user)
    with pytest.raises(IntegrityError) as ex:
        db.session.commit()
    assert "UNIQUE constraint failed" in str(ex.value)
    db.session.rollback()


def test_admin_user_new_without_name(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user_without_name = User(email="teste@teste.com")
    db.session.add(user_without_name)
    with pytest.raises(IntegrityError) as excinfo:
        db.session.commit()
    assert "NOT NULL" in str(excinfo.value)
    db.session.rollback()


def test_admin_user_new_without_email(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user_without_email = User(name="Revton sem email")
    db.session.add(user_without_email)
    db.session.commit()
    assert "<User(name=Revton sem email, email=None)>" == repr(
        User.query.filter_by(name="Revton sem email").first()
    )


def test_admin_user_new_without_data(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user_without_data = User()
    db.session.add(user_without_data)
    with pytest.raises(IntegrityError) as excinfo:
        db.session.commit()
    assert "NOT NULL" in str(excinfo.value)
    db.session.rollback()
