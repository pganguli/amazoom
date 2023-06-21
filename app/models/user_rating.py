from app.extensions import db
from app.models.user import User
from app.models.product import Product


class UserRating(db.Model):
    id = db.Column(db.Integer,
                   autoincrement=True, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id),    nullable=False)
    product_id = db.Column(db.ForeignKey(Product.id), nullable=False)
    review = db.Column(db.String)
