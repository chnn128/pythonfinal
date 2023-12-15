# pythonfinal

This app takes in a playlist of less than 50 tracks in length and sorts by danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, or tempo (when run from the web app) or simply danceability (run from the command line).

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```


Install packages:
```sh
pip install -r requirements.txt
```

Credentials: 
Obtain an [API Key from Spotify](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).

You must first follow the [setup instructions](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to create an app, request an access token (API KEY), and use the token to request data. You should have a client ID and a client secret.

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

#Place your client ID here in this variable
cid="_________"

#Place your client secret here in this variable
csecret="____"

```

## Usage

Run the project from the command line:

```sh
python -m app.main_app

```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

Details about the web app can be seen in the browser once launched! 

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```
