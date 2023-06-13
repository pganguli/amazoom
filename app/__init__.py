from flask import Flask
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    # Initialize Flask extensions

    from app.extensions import db
    db.init_app(app)

    # Within app context
    with app.app_context():
        # Before first request

        from app.models.user import User
        from app.models.product import Product
        db.create_all()

        # Register bluprints

        from app.blueprints.main import bp as main_bp
        app.register_blueprint(main_bp)

        from app.blueprints.auth import bp as auth_bp
        app.register_blueprint(auth_bp)

        from app.blueprints.user import bp as user_bp
        app.register_blueprint(user_bp)

        from app.blueprints.product import bp as product_bp
        app.register_blueprint(product_bp)

        return app
