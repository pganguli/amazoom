from flask import Flask
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    # Initialize Flask extensions
    from app.extensions import db
    db.init_app(app)

    with app.app_context():
        # Before first request
        from app.models.user import User
        from app.models.product import Product
        db.create_all()

        # Register bluprints
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)

        return app
