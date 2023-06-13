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

from app.models.donor import Donor
from app.models.receipt import Receipt


@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@bp.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@bp.route("/favicon.ico")
def favicon() -> Response:
    return send_from_directory(
        os.path.join(bp.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/")
def index() -> Response:
    return make_response(render_template("index.html"))


@bp.route("/list")
def list_receipt() -> Response:
    # Search by receipt serial number
    serial: str = request.args.get("serial", "")
    return make_response(render_template("list.html", serial=serial))


@bp.route("/receipt", methods=["GET", "POST"])
def receipt() -> Response:
    # Results for a specific serial number
    if request.method == "POST":
        serial: str = request.form.get("serial", "")
        receipt: Receipt | None = Receipt.query.filter(
            (Receipt.serial == serial) & (Receipt.canceled is not True)
        ).first()
        if receipt is None:
            flash("Requested serial number not found!")
            return make_response(render_template("list.html", serial=serial))
        else:
            donor: Donor | None = Donor.query.filter(
                (Donor.id == receipt.donor_id)
            ).first()
            return make_response(
                render_template("print_receipt.html", receipt=receipt, donor=donor)
            )
    # Search by receipt serial number
    else:
        receipts: list[Receipt] = Receipt.query.filter(
            (db.func.date(Receipt.datetime) == date.today())
            & (Receipt.canceled is not True)
        ).all()
        receipts.sort(key=lambda k: k.datetime, reverse=True)
        return make_response(render_template("receipt.html", receipts=receipts))


@bp.route("/print", methods=["POST"])
def printed() -> Response:
    serial: str = request.form.get("serial", "")
    receipt: Receipt | None = Receipt.query.filter(
        (Receipt.serial == serial) & (Receipt.canceled is not True)
    ).first()
    if receipt is None:
        abort(404, description="Receipt not found")
    try:
        receipt.printed = True
        db.session.commit()
    except exc.IntegrityError:
        abort(400, description="Malformed receipt given")
    return make_response("")


@bp.route("/cancel", methods=["POST"])
def canceled() -> Response:
    serial: str = request.form.get("serial", "")
    receipt: Receipt | None = Receipt.query.filter(
        (Receipt.serial == serial) & (Receipt.canceled is not True)
    ).first()
    if receipt is None:
        return make_response(redirect("/receipt"))
    try:
        receipt.canceled = True
        db.session.commit()
    except exc.IntegrityError:
        return make_response(redirect("/receipt"))
    return make_response(redirect("/receipt"))
