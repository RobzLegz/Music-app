from flask import Blueprint, render_template, request, flash, redirect, session, flash, url_for

from components.music.models import Artist

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/artists", methods=["GET", "POST"])
def artists():
    if session.get("is_admin"):
        if request.method == "POST":
            form_data = request.form
            artist_name = form_data.get("name")
            artist_about = form_data.get("about")
            artist_image = form_data.get("image")
            artist_birthday = str(form_data.get("birthday"))

            if artist_name != "" and artist_about != "" and artist_image != "" and artist_birthday != "":
                new_artist = Artist.create(
                    name=artist_name,
                    about=artist_about,
                    image=artist_image,
                    birth_data=artist_birthday,
                )

                flash(f"Artist {new_artist.name} created!", "success")
            else:
                flash("OOOOPS, something went wrong!", "danger")

        artists = Artist.select()

        context = {
            "artists": artists
        }

        return render_template("music/admin/artists.html", **context)

    return redirect(url_for("home.index"))


@admin.route("/songs", methods=["GET", "POST"])
def songs():
    if session.get("is_admin"):
        if request.method == "POST":
            pass

        return render_template("music/admin/songs.html")

    return redirect(url_for("home.index"))


@admin.route("/albums", methods=["GET", "POST"])
def albums():
    if session.get("is_admin"):
        if request.method == "POST":
            pass

        return render_template("music/admin/albums.html")

    return redirect(url_for("home.index"))