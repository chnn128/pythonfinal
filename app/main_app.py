# this is the main python script 
import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from operator import itemgetter
from IPython.display import Image, display




def fetch_spotify_data(cid, csecret, playlist_URL, attribute):
    '''
    This is the main python function. It takes in API credentials, playlist url, and desired attribute as strings. 
    It requests playlist and song information from the Spotify API, then returns the playlist in a list from sorted by attribute.
    '''

    #setting up credentials for API
    c_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
    sp = spotipy.Spotify(client_credentials_manager = c_credentials_manager)



    #Grabbing tracks / track URIs
    #playlist_URL = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"  ### example playlist
    playlist_URI = playlist_URL.split("/")[-1].split("?")[0] #extracting URI from URL
    playlist_tracks_info = sp.playlist_tracks(playlist_URI)["items"]
    track_uris = [x["track"]["uri"] for x in playlist_tracks_info]



    #using track uri list to generate list of tracks w/ audio features
    tracks_attributes = sp.audio_features(track_uris)



    #sorting the audio features list by 'attribute'
    sorted_tracks_attributes = sorted(tracks_attributes, key = itemgetter(attribute), reverse = True)



    #isolating the sorted track uris and attribute scores - not super efficient at the moment
    sorted_track_uris = []
    sorted_track_attributerating = []
    
    for track in sorted_tracks_attributes:
        sorted_track_uris.append(track['uri'])
        sorted_track_attributerating.append(track[attribute])



    #grabbing the track information of the sorted tracks
    sorted_tracks_infos = sp.tracks(sorted_track_uris)['tracks']



    #appending track info and danceability ratings to a return list
    final_return = []
    n = 0
   
    for track in sorted_tracks_infos:
        final_return.append({'Name': track['name'],
                      'Artist': track['artists'][0]['name'],
                      'Album': track['album']['name'],
                      'Thumbnail': track['album']['images'][1]['url'],
                      'Attribute': sorted_track_attributerating[n],
                      'SongURL': track['external_urls']['spotify']})
        n = n + 1

    #returning the sorted playlist
    return final_return





if __name__ == "__main__":


    load_dotenv()

    CID = str(os.getenv("CID"))
    CSECRET = str(os.getenv("CSECRET"))

    print("Welcome to our app! Running it from the command line will result in sorting by danceability. For more functionality, please launch the web app.")
    PLAYLIST_URL = input("Please enter playlist URL: ")
    
    

    final_return =  fetch_spotify_data(cid = CID, csecret = CSECRET, playlist_URL = PLAYLIST_URL, attribute = 'danceability')

    for track in final_return:
        print('\n---------')
        display(Image(url=track['Thumbnail'], height=300))
        print(f" Name: {track['Name']} \n Artist: {track['Artist']} \n Album: {track['Album']} \n Attribute Rating: {track['Attribute']} \n" )
