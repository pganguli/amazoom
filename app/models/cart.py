from app.extensions import db
from app.models.user import User
from app.models.product import Product


class Cart(db.Model):
    id          = db.Column(db.Integer,                autoincrement=True, primary_key=True)
    user_id     = db.Column(db.ForeignKey(User.id),    nullable=False)
    product_id  = db.Column(db.ForeignKey(Product.id), nullable=False)
    quantity    = db.Column(db.Integer,                nullable=False)
    fixed_price = db.Column(db.Float,                  nullable=False)

    def __repr__(self):
        return f"<Cart(id='{self.id}', user_id='{self.user_id}', product_id='{self.product_id}')>"
