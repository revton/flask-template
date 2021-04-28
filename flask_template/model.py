"""Module db Model."""
from flask_template.extensions.database import db


class User(db.Model):
    """Class User."""

    ___tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String())

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
