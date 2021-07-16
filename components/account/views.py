from flask import Blueprint, render_template, request, flash
import re

from flask.helpers import flash

account = Blueprint("account", __name__)


@account.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print(request.form)

    return render_template("login.html")


@account.route("/register", methods=["GET", "POST"])
def register():
    error_messages = []

    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        email = form_data.get("email")
        password = form_data.get("password")
        remember_me = form_data.get("remember")

        print(username, email, password, remember_me)

        username_err = ""
        email_err = ""
        password_err = ""

        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email)

        if username == "":
            if len(emails) == 0:
                email_err = "Please provide a valid email"
                error_messages.append(email_err)
            if len(password) < 6:
                password_err = "Your password should be at least 6 characters long"
                error_messages.append(password_err)
            username_err = "Please provide your username"
            error_messages.append(username_err)

        elif len(emails) == 0:
            email_err = "Please provide a valid email"
            error_messages.append(email_err)

            if len(password) < 6:
                password_err = "Your password should be at least 6 characters long"
                error_messages.append(password_err)

        elif len(password) < 6:
            password_err = "Your password should be at least 6 characters long"
            error_messages.append(password_err)
        

        if len(error_messages) > 0:
            for err in error_messages:
                flash(err)

    return render_template("register.html")
            
        

    