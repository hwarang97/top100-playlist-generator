from bs4 import BeautifulSoup


class Parser:
    def __init__(self, webpage:str):
        self.webpage = webpage
        self.features = "html.parser"
        self.soup = BeautifulSoup(markup=self.webpage, features=self.features)

    def get_artists(self) -> list[str]:
        artists = self.soup.find_all("p", class_="artist")
        artist_list = [artist.get_text().strip() for artist in artists]
        return artist_list

    def get_albums(self) -> list[str]:
        albums = self.soup.find_all("a", class_="album")
        album_list = [album.get_text().strip() for album in albums[1:]]
        return album_list

    def get_titles(self) -> list[str]:
        titles = self.soup.find_all("p", class_="title")
        title_list = [title.get_text().strip() for title in titles]
        return title_list

    def get_top100(self) -> list[dict]:
        artist_list = self.get_artists()
        album_list = self.get_albums()
        title_list = self.get_titles()

        articles = self.soup.find_all("p", class_="title")
        top100_playlist = [{"title" : title, "album": album, "artist": artist} for title, album, artist in zip(title_list, album_list, artist_list)]
        return top100_playlist
