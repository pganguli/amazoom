import os
from datetime import date

from flask import make_response
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import redirect
from flask import flash
from flask import jsonify
from flask import abort
from flask import Response

from sqlalchemy import exc

from app.main import bp
from app.extensions import db

from app.models.user import User
from app.models.product import Product


@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@bp.errorhandler(400)
def bad_request(e):
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
    return make_response(render_template("index.html"))


@bp.route("/cart")
def list_receipt() -> Response:
    return make_response(render_template("cart.html"))
