import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import threading
import subprocess


from dotenv import load_dotenv
load_dotenv()
 
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


track_list = set()


if not client_id or not client_secret:
    raise RuntimeError(
        "Missing CLIENT_ID or CLIENT_SECRET. "
        "Create a .env file based on .env.example."
    )

def Download_Song(track_url, track_length, song):
    if track_length >= 10:
        print("Track is too long!")
        return

    cmd = [
        "spotdl",
        "--client-id", client_id,
        "--client-secret", client_secret,
        track_url
    ]

    try:
        print("Downloading track:", track_url)
        ret = subprocess.run(cmd, capture_output=True, text=True)
        if ret.returncode == 0:
            print(song, "Downloaded")
            print("Standby...")
        else:
            print("[spotdl error]", ret.stderr or ret.stdout)
    except Exception as e:
        print("Track not found...", e)



def AddSong(track_name,track_url,artist_name):
    track_list.add(track_url)
    song = (f"{track_name} by {artist_name}")
    print(song," Was found in the playlist")
    
    return song


class Spotify(object):
    cid = client_id
    secret = client_secret
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    def Playlist_Data(playlist_link):
        sp = Spotify.sp
        
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]

        for track in sp.playlist_tracks(playlist_URI)["items"]:
            #Track URL
            track_url = track["track"]["external_urls"]["spotify"]
            #Track name & artist
            track_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]
            
            #Track duration in minutes
            track_length = track["track"]["duration_ms"] / 60000
    
            if track_url not in track_list:
                try:
                    song = AddSong(track_name, track_url, artist_name)
                    t = threading.Thread(target=Download_Song,args=(track_url,track_length,song,), daemon=True) 
                    t.start()
                    
                
                except Exception as e:
                    print("An error has occurred:", e)
            else:
                continue 


playlist_link = input('Paste playlist link here(public spotify playlist where people will add requests): ') 

while True:
   Spotify.Playlist_Data(playlist_link)
   time.sleep(30)


