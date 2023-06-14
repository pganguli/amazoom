from flask import make_response
from flask import render_template
from flask import jsonify
from flask import Response

from flask_login import login_required
from flask_login import current_user

from app.blueprints.user import user_bp

from app.models.cart import Cart
from app.models.product import Product


@user_bp.errorhandler(404)
def bad_request(e) -> tuple[Response, int]:
    return jsonify(error=str(e)), 404


@user_bp.route("/cart")
@login_required
def index() -> Response:
    cart: list[Cart] = Cart.query.filter(Cart.user_id == current_user.id).all()
    products: list[Product] = []
    for cart_item in cart:
        products.append(Product.query.get(cart_item.product_id))
    return make_response(render_template("user/cart.html", user=current_user, cart=cart, products=products))
