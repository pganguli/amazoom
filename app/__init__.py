from flask import Flask
from config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class)

    # Initialize Flask extensions

    from app.models.user import User
    from app.models.product import Product
    from app.models.cart import Cart

    from app.extensions import db
    db.init_app(app)

    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Within app context
    with app.app_context():
        # Before first request

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
