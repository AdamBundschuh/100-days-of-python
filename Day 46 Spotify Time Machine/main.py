from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Passwords import authentication as auth
from pprint import pprint

AUTH = auth.music_time_machine['spotipy']
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIPY_CLIENT_ID = AUTH['spotipy_client_id']
SPOTIPY_CLIENT_SECRET = AUTH['spotipy_client_secret']
SPOTIPY_REDIRECT_URI = "http://example.com"
SPOTIPY_SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SPOTIPY_SCOPE,
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]

print("Welcome to the Music Time Machine!")
user_input = input("Please enter a date in the format YYYY-MM-DD: ").split("-")
YEAR = user_input[0]
MONTH = user_input[1]
DAY = user_input[2]
print(f"{YEAR} {MONTH} {DAY}")

URL = f"https://www.billboard.com/charts/hot-100/{YEAR}-{MONTH}-{DAY}/"
print(URL)

response = requests.get(URL)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

songs = [h3.get_text().strip() for h3 in soup.select('h3[class*="a-no-trucate"]')]
artists = [span.get_text().strip() for span in soup.select('span[class*="a-no-trucate"]')]
combined_list = [{"artist": artist, "song": song} for song, artist in zip(songs, artists)]
# Created a list of dictionaries to avoid songs with the same name causing a bug

playlist_name = f"{MONTH}-{DAY}-{YEAR} TOP 100 BILLBOARD"
playlist_desc = "Top tracks from the past."
playlist_id = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_desc)['uri']

song_uris = []
print(f"Gathering song URIS :: Start")

for i, dict in enumerate(combined_list):
    track = sp.search(q=f'track: {dict["song"]} artist: {dict["artist"]} year: {YEAR}', type="track", limit=1)['tracks']['items'][0]['uri']
    print(f"  #{i+1}: {dict['song']} :: {track}")
    song_uris.append(track)

print(f"Gathering song URIS :: End")
sp.playlist_add_items(playlist_id, song_uris)
