# this is the "web_app/routes/weather_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.main_app import main

spotify_routes = Blueprint("spotify_routes", __name__)


@spotify_routes.route("/spotify/form")
def spotify_form():
    print("SPOTIFY FORM...")
    return render_template("spotify_form.html")