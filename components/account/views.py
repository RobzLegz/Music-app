from flask import Blueprint, render_template

account = Blueprint("account", __name__)


@account.route("/login")
def login():
    return render_template("login.html", title="Login")


@account.route("/register")
def register():
    return render_template("register.html", title="Register")