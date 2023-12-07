#this script takes in all user inputs

import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from operator import itemgetter
from IPython.display import Image, display




def fetch_spotify_data(cid, csecret, playlist_URL):

    c_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
    sp = spotipy.Spotify(client_credentials_manager = c_credentials_manager)


    #Grabbing tracks / track URIs

    #playlist_URL = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"  ### example playlist

    playlist_URI = playlist_URL.split("/")[-1].split("?")[0] #extracting URI from URL
    playlist_tracks_info = sp.playlist_tracks(playlist_URI)["items"]
    track_uris = [x["track"]["uri"] for x in playlist_tracks_info]




    #using track uri list to generate list of tracks w/ audio features
    tracks_attributes = sp.audio_features(track_uris)




    #sorting the audio features list by 'danceability'
    sorted_tracks_attributes = sorted(tracks_attributes, key = itemgetter('danceability'), reverse = True)
    sorted_tracks_attributes[0] #just to examine the different possibilities




    #isolating the sorted track uris and danceability scores - not super efficient at the moment
    sorted_track_uri_attributerating = []
    sorted_track_uris = []
    sorted_track_attributerating = []

    for track in sorted_tracks_attributes:
        sorted_track_uri_attributerating.append([track['uri'], track['danceability']])
        sorted_track_uris.append(track['uri'])
        sorted_track_attributerating.append(track['danceability'])

    #grabbing the track information of the sorted tracks
    sorted_tracks_infos = sp.tracks(sorted_track_uris)['tracks']

    sorted_tracks_infos[0].keys() #just peeking and exploring
    sorted_tracks_infos[0]['album'].keys() #just peeking and exploring

    #appending track info and danceability ratings to a return list
    final_return = []
    n = 0
   
    for track in sorted_tracks_infos:
        final_return.append({'Name': track['name'],
                      'Artist': track['artists'][0]['name'],
                      'Album': track['album']['name'],
                      'Thumbnail': track['album']['images'][1]['url'],
                      'Danceability': sorted_track_attributerating[n]})
        n = n + 1

    #returning the sorted playlist
    return final_return





if __name__ == "__main__":

    load_dotenv()

    CID = str(os.getenv("CID"))
    CSECRET = str(os.getenv("CSECRET"))

    PLAYLIST_URL = input("Please enter playlist URL: ")

    final_return =  fetch_spotify_data(cid = CID, csecret = CSECRET, playlist_URL = PLAYLIST_URL)

    for track in final_return:
        print('\n---------')
        display(Image(url=track['Thumbnail'], height=300))
        print(f" Name: {track['Name']} \n Artist: {track['Artist']} \n Album: {track['Album']} \n Danceability Rating: {track['Danceability']} \n" )
