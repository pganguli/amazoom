from flask import make_response
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import abort
from flask import jsonify
from flask import Response

from flask_login import login_user

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.blueprints.auth import bp

from app.extensions import db
from app.models.user import User


@bp.errorhandler(400)
def bad_request(e) -> tuple[Response, int]:
    return jsonify(error=str(e)), 400


@bp.route("/login")
def login() -> Response:
    return make_response(render_template("auth/login.html"))


@bp.route('/login', methods=['POST'])
def login_post():
    email: str | None = request.form.get('email')
    password: str = request.form.get('password', "")
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash("User does not exist or incorrect password supplied.")
        return make_response(redirect(url_for('auth.login')))

    login_user(user, remember=remember)

    return redirect(url_for('main.index'))


@bp.route("/register")
def register() -> Response:
    return make_response(render_template("auth/register.html"))


@bp.route("/register", methods=["POST"])
def register_post() -> Response:
    name: str | None = request.form.get("name")
    email: str | None = request.form.get("email")
    password: str = request.form.get("password", "")

    if password == "":
        abort(400, description="No password supplied.")

    user = User.query.filter_by(email=email).first()
    if user:
        flash("Email address already exists.")
        return make_response(redirect(url_for("auth.register")))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="sha256"),
    )
    db.session.add(new_user)
    db.session.commit()

    return make_response(redirect(url_for("auth.login")))
