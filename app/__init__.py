from flask import Flask
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    # Initialize Flask extensions

    from app.models.user import User
    from app.models.product import Product
    from app.models.cart import Cart
    from app.models.prodct_rating import ProductRacting
    from app.models.user_rating import UserRating

    from app.extensions import db

    db.init_app(app)

    from app.extensions import login_manager

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: str):
        try:
            return User.query.get(int(user_id))
        except ValueError:
            pass
        return None

    # Within app context
    with app.app_context():
        # Before first request

        db.create_all()

        # addProducts()

        rows = [
            ("Smartwatch", 15000, 100, "app/static/assets/smartwatch.jpeg"),
            ("Earphones", 3000, 200, "app/static/assets/earphones.jpeg"),
            ("Keyboard", 1500, 100, "app/static/assets/keyboard.jpeg"),
            ("Tablet", 20000, 50, "app/static/assets/tablet.jpeg"),
            ("Headphones", 5000, 200, "app/static/assets/headphones.jpeg"),
            ("Yoga mat", 500, 100, "app/static/assets/yoga.jpeg"),
            ("Jumprope", 300, 100, "app/static/assets/jumprope.jpeg"),
            ("Shoes", 3500, 200, "app/static/assets/shoes.jpeg"),
            ("Kettlebell", 700, 50, "app/static/assets/kettlebell.jpeg"),
            ("Dumbell", 700, 50, "app/static/assets/dumbell.jpeg"),
            ("Guitar", 1500, 100, "app/static/assets/guitar.jpeg"),
            ("Piano", 35000, 50, "app/static/assets/piano.jpeg"),
            ("Violin", 2000, 100, "app/static/assets/violin.jpeg"),
            ("Saxophone", 3500, 100, "app/static/assets/saxophone.jpeg"),
            ("Drums", 5050, 500, "app/static/assets/drums.jpeg")
        ]
        for i in rows:
            db.session.add(Product(name=i[0], price=i[1], stock=i[2], image=i[3]))
        db.session.commit()

        # Register bluprints

        from app.blueprints.main import main_bp

        app.register_blueprint(main_bp)

        from app.blueprints.auth import auth_bp

        app.register_blueprint(auth_bp)

        from app.blueprints.user import user_bp

        app.register_blueprint(user_bp)

        from app.blueprints.product import product_bp

        app.register_blueprint(product_bp)

        return app
