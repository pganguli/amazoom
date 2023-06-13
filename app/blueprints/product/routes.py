from flask import make_response
from flask import render_template
from flask import Response

from app.blueprints.product import bp

from app.models.product import Product


@bp.route("/product")
def product() -> Response:
    return make_response("")
