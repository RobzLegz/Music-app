from flask import Blueprint, render_template, request, flash, redirect, session
import re

from flask.helpers import flash, url_for

account = Blueprint("account", __name__)


@account.route("/login", methods=["GET", "POST"])
def login():
    error_messages = []

    if request.method == "POST":
        form_data = request.form
        email = form_data.get("email")
        password = form_data.get("password")

        if email == "admin123@gmail.com" and password == "password":
            session["logged_in"] = True
            session["is_admin"] = True
            session["user_email"] = "admin"
            
            return redirect(url_for("home.index"))


        email_err = ""
        password_err = ""

        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email)

        if len(emails) == 0:
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
                flash(err, "danger")

    return render_template("auth/login.html")


@account.route("/register", methods=["GET", "POST"])
def register():
    error_messages = []

    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        email = form_data.get("email")
        password = form_data.get("password")
        remember_me = form_data.get("remember")

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
                flash(err, "danger")
        else:
            session["logged_in"] = True
            session["user_email"] = email
            return redirect(url_for("home.index"))

    return render_template("auth/register.html")

@account.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear() 

    return redirect(url_for("account.login"))
        

    