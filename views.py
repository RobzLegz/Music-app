from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("base.html")


@views.route("/login")
def login():
    return render_template("login.html")


@views.route("/register")
def register():
    return render_template("register.html")