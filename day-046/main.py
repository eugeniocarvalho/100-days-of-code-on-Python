import pprint
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = "http://example.com"
USERNAME_ID = "3kb8l19ngzfptphbcprn93b4h"

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

search_str = ""

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


date = input("Which year do you want to travel to? Tupe the data in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp.user_playlist_create(user=USERNAME_ID, name=f"{date} Billboard 100")

PLAYLIST_ID = sp.current_user_playlists()["items"][0]["id"]

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

song_titles = [title.getText().strip() for title in soup.select("li #title-of-a-story")]
song_artists = [artist.getText().strip() for artist in soup.select("li .c-label.a-no-trucate")]

songs_uri = []

for i in range(100):
  result = sp.search(f"{song_titles[i]} {song_artists[i]}", limit=2)
  songs_uri.append(result["tracks"]["items"][0]["uri"])

sp.user_playlist_add_tracks(USERNAME_ID, playlist_id=PLAYLIST_ID, tracks=songs_uri)