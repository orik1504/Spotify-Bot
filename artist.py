""" 
Artist class will include:
* number of albums + names of top 5 (from album class)
* Top 5 songs (from song class) 
* Spotify link
* best album by listeners
* monthly listeners
 """

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from client_id import Client

client = Client()

SPOTIPY_CLIENT_ID = client.get_client_id()
SPOTIPY_CLIENT_SECRET = client.get_client_secret()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))


class Artist():

    def __init__(self, name: str):
        self.name = name
        self.uri = self.__get_uri()

    def __get_uri(self):
        """ Define the URI of the given artist """
        return sp.search(q=self.name, type="artist").get(
            "artists").get("items")[0].get("id")

    def num_of_albums(self):
        """ returns the number of the albums of the artist and names of the albums """
        # TODO: need to add number of albums
        # TODO: need to deal with duplicates
        return [album["name"] for album in sp.artist_albums(self.uri).get("items")]

    def top_5_albums(self):
        """ gets list of the 5 top albums of the artist, returns the names, 
        publish date, how much listeners, how much time for an album by time
        and albums cover  """
        pass

    def top_5_songs(self,):
        """ gets a list of the  top 5 songs of the artist by the listeners count
        returns the name, length of the song, publish date, cover, in what album is the song in
        """
        pass

    def spotify_link(self,):
        """ returns the spotify link of the artist """
        pass

    def best_album(self):
        """ return the best album of the artist
        returns name, cover, publish date, length of the album by time, best song by the listeners """
        pass

    def monthly_listeners(self):
        """ returns the number of monthly listeners """
        pass
