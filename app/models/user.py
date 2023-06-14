from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name     = db.Column(db.String,  nullable=False)
    email    = db.Column(db.String,  nullable=False, unique=True)
    password = db.Column(db.String,  nullable=False)
    address  = db.Column(db.String)

    def __repr__(self):
        return f"<User(id='{self.id}', email='{self.email}')>"
