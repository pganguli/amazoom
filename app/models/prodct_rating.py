from app.extensions import db
from app.models.product import Product


class ProductRacting(db.Model):
    id = db.Column(db.Integer,
                   autoincrement=True, primary_key=True)
    product_id = db.Column(db.ForeignKey(Product.id), nullable=False)
    rating_1 = db.Column(db.Integer)
    rating_2 = db.Column(db.Integer)
    rating_3 = db.Column(db.Integer)
    rating_4 = db.Column(db.Integer)
    rating_5 = db.Column(db.Integer)
