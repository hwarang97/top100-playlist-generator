from spotify_search import SpotifySearch
from web_parser import Parser
from bugs_search import BugsSearch
from datetime import datetime

# Authentication
sp = SpotifySearch()
user_info = sp.get_search().current_user()

# load webpage
target_date = input("Which year do you want to travel to? Type the date in this format YYYYMMDD: ")
bugs_search = BugsSearch(target_date)
webpage = bugs_search.get_webpage()

# parsing top100 tracks
parser = Parser(webpage=webpage)
top100_playlist = parser.get_top100()

# search
type = "track"
track_uri_list = []
for track in top100_playlist:
    track_uri = sp.get_track_uri(track=track["title"], type=type)
    if track_uri:
        track_uri_list.append(track_uri)

# create new playlist
formmated_date = datetime.strptime(target_date, "%Y%m%d").strftime("%Y-%m-%d")
name = f"{formmated_date} Bugs 100"
playlist = sp.get_search().user_playlist_create(user=user_info.get("id"), name=name)

# # add track to my playlist
playlist_id = playlist.get("id")
sp.add_items(playlist_id=playlist_id, items=track_uri_list)
