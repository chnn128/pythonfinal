# pythonfinal

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

Obtain an [API Key from Spotify](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).

You must first follow the [setup instructions](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) to create an app, request an access token (API KEY), and use the token to request data.

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

#client ID
cid="_________"

#client secret
csecret="____"

```


## Usage

Run the example script:

```sh
python -m app.app

```


## Testing

Run tests:

```sh
pytest
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```