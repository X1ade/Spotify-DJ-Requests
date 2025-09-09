import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import threading

from dotenv import load_dotenv
load_dotenv() # ensures enviroment variables in .env can be used, better then hardcoding secrtet values
 
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
track_list = []

def Download_Song(track_url,track_length,song):
    try:
        if track_length < 10:
            os.system ("spotdl "+ track_url)
            time.sleep(10)
            print(song,' Downloaded')
            print('Standby...')
        else:
            print("Track is too long!")
    except:
        print('Track not found :(')

def AddSong(track_name,track_url,artist_name):
    track_list.append(track_url)
    song = (track_name,artist_name)
    print(song)
    print(track_url)
    return song


class Spotify(object):
    cid = client_id
    secret = client_secret
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    def Playlist_Data(playlist_link):
        sp = Spotify.sp
        #playlist_link = "https://open.spotify.com/playlist/05SmegprCOFAFpOo9VIAxT?si=4a2504afe4184c90"
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        track_uris = [x["track"]["uri"] 
        for x in sp.playlist_tracks(playlist_URI)["items"]]
        for track in sp.playlist_tracks(playlist_URI)["items"]:
            #Track URL
            track_url = track["track"]["external_urls"]["spotify"]
            #Track name & artist
            track_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]

            #Track duration in minutes
            track_length = track["track"]["duration_ms"] / 60000
        
        check = False
        
        if len(track_list) > 0:
            for i in range (0,len(track_list)):
                if track_url != track_list[i]:
                    check = True
                else:
                    check = False
                    break
        else:
            try:
                song = AddSong(track_name, track_url,artist_name)
                t = threading.Thread(target=Download_Song,args=(track_url,track_length,song,), daemon=True) 
                t.start()      
            except:
                print('No tracks')

        if check:
            song = AddSong(track_name, track_url,artist_name)
            t = threading.Thread(target=Download_Song,args=(track_url,track_length,song,), daemon=True)
            t.start()   
  
        
playlist_link = input('Paste playlist link here(public spotify playlist where people will add requests): ') 

while True:
   Spotify.Playlist_Data(playlist_link)
   time.sleep(60)


