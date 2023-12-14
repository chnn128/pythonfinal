import os
from dotenv import load_dotenv


from app.main_app import fetch_spotify_data

def test_fetch_spotify_data():
    load_dotenv()
    CID = str(os.getenv("CID"))
    CSECRET = str(os.getenv("CSECRET"))
    
    PLAYLIST_URL = "https://ophttps://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7fen.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    ATT = 'tempo'

    result = fetch_spotify_data(cid = CID, csecret = CSECRET, playlist_URL = PLAYLIST_URL, attribute = ATT)

    assert isinstance(result, list) == True
    assert isinstance(result[0], dict) == True
    assert 'Name' in result[0].keys()
    assert 'Artist' in result[0].keys()
    assert 'Album' in result[0].keys()
    assert 'Thumbnail' in result[0].keys()
    assert 'Attribute' in result[0].keys()
    assert 'SongURL' in result[0].keys()


