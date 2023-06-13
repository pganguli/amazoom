from app.extensions import db


class Donor(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pan = db.Column(db.String, unique=True)
    aadhaar = db.Column(db.String, unique=True)
    mobile = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    address = db.Column(db.String)
