import os

from flask import make_response
from flask import render_template
from flask import send_from_directory
from flask import jsonify
from flask import Response

from app.blueprints.main import bp

from app.models.product import Product


@bp.errorhandler(400)
def bad_request(e) -> tuple[Response, int]:
    return jsonify(error=str(e)), 400


@bp.route("/favicon.ico")
def favicon() -> Response:
    return send_from_directory(
        os.path.join(bp.root_path, "static/assets"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/")
def index() -> Response:
    products: list[Product] = Product.query.all()
    return make_response(render_template("main/index.html", products=products))
