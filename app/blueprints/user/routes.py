from flask import make_response
from flask import render_template
from flask import jsonify
from flask import Response

from app.blueprints.main import bp

from app.models.user import User
from app.models.cart import Cart


@bp.errorhandler(400)
def bad_request(e) -> tuple[Response, int]:
    return jsonify(error=str(e)), 400


@bp.route("/cart")
def index() -> Response:
    cart: list[Cart] = Cart.query.filter(Cart.user_id == user.id).all()
    return make_response(render_template("user/cart.html", cart=cart))
