from dotenv import load_dotenv
from spotipy import SpotifyOAuth
import spotipy
import os


class SpotifySearch:
    def __init__(self):
        load_dotenv()
        self.scope = "playlist-modify-public"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT"),
            client_secret=os.getenv("SPOTIFY_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT"),
            scope=self.scope, ))

    def get_search(self):
        return self.sp

    def get_track_uri(self, track: str, type: str) -> str | None:
        query = f"track:{track}"
        response = self.sp.search(q=query, type=type)
        try:
            track_uri = response["tracks"]["items"][0]["uri"]
            return track_uri
        except IndexError:
            print(f"song: {track} does not exist in Spotify. Skipped.")

    def add_items(self, playlist_id: str, items: list[str]):
        self.sp.playlist_add_items(playlist_id=playlist_id, items=items)

