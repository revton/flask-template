from flask_template.model import User


def test_admin_update_user_valid(test_client):
    app = test_client.application
    db = app.extensions["sqlalchemy"].db
    # Create user
    user = User(name="Revton", email="revtonbr@gmail.com")
    db.session.add(user)
    db.session.commit()
    # Find and update user
    user = User.query.filter_by(name="Revton").first()
    user.name = "Revton atualizado"
    user.email = "revtonbr_atualizado@gmail.com"
    db.session.commit()
    assert (
        "<User(name=Revton atualizado, email=revtonbr_atualizado@gmail.com)>"
        == repr(User.query.filter_by(name="Revton atualizado").first())
    )
