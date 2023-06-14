from app.extensions import db


class Product(db.Model):
    id       = db.Column(db.Integer, autoincrement=True, primary_key=True)
    price    = db.Column(db.Float,   nullable=False)
    stock    = db.Column(db.Integer, nullable=False)
    name     = db.Column(db.String,  nullable=False)
    desc     = db.Column(db.String)
    rating_1 = db.Column(db.Integer)
    rating_2 = db.Column(db.Integer)
    rating_3 = db.Column(db.Integer)
    rating_4 = db.Column(db.Integer)
    rating_5 = db.Column(db.Integer)

    def __repr__(self):
        return f"<Product(id='{self.id}', name='{self.name}')>"
