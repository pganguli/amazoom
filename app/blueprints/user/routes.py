from flask import make_response
from flask import render_template
from flask import jsonify
from flask import Response

from flask_login import login_required
from flask_login import current_user

from app.blueprints.user import bp

from app.models.cart import Cart


@bp.errorhandler(400)
def bad_request(e) -> tuple[Response, int]:
    return jsonify(error=str(e)), 400


@bp.route("/cart")
@login_required
def index() -> Response:
    cart: list[Cart] = Cart.query.filter(Cart.user_id == current_user.id).all()
    return make_response(render_template("user/cart.html", cart=cart))
