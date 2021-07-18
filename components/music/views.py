from flask import Blueprint, render_template, request, flash, redirect, session

from flask.helpers import flash, url_for

music = Blueprint("music", __name__, url_prefix="/music")

@music.route("/artists", methods=["GET", "POST"])
def artists():
    return render_template("admin_base.html")