# -*- coding: utf-8 -*-
from flask_template.model import User


def test_admin_remove_user_valid(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    user = User.query.filter_by(name="Revton").first()
    db.session.delete(user)
    db.session.commit()
    assert len(User.query.filter_by(name="Revton").all()) == 0
