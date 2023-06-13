from app.extensions import db
from app.models.donor import Donor


class Receipt(db.Model):
    serial = db.Column(db.Integer, autoincrement=True, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    place = db.Column(db.String)
    donor_id = db.Column(db.ForeignKey(Donor.id), nullable=False)
    paymethod = db.Column(db.String, nullable=False)
    purpose = db.Column(db.String, nullable=False)
    bank = db.Column(db.String)
    docnum = db.Column(db.String)
    printed = db.Column(db.Boolean, nullable=False)
    canceled = db.Column(db.Boolean, nullable=False)
