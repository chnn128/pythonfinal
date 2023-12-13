# this is the "web_app/routes/spotify_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.main_app import os, fetch_spotify_data

spotify_routes = Blueprint("spotify_routes", __name__)


@spotify_routes.route("/spotify/form")
def spotify_form():
    print("SPOTIFY FORM...")
    return render_template("spotify_form.html")

@spotify_routes.route("/spotify/dashboard", methods=["GET", "POST"])
def spotify_dashboard():
    print("SPOTIFY REPORTS")

    if request.method == "POST":
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    playlist_url = request_data.get("playlist_url")
    song_characteristic = request_data.get("song_characteristic")
    CID = str(os.getenv("CID"))
    CSECRET = str(os.getenv("CSECRET"))

    try:
        data = fetch_spotify_data(cid=CID, csecret=CSECRET, playlist_URL=playlist_url, attribute = song_characteristic)

        flash("Fetched Latest Spotify Data!", "success")
        return render_template("spotify_dashboard.html", data=data)

    except Exception as err:
        print('OOPS', err)

        flash("URL Error. Please check your playlist and try again!", "danger")
        return redirect("/spotify/form")

@spotify_routes.route("/api/spotify.json")
def spotify_api():
    print("SPOTIFY API DATA")

    try:
        data = fetch_spotify_data()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Data Error. Please try again."}, 404