""" 
Song class will include :
* song length by time of listening
* title of song 
* song cover (as a picture)
* artist 
* in what album the song
* link on spotify
* when the song got out
 """

import tekore as tk
from client_id import Client

client = Client()

client_id = client.get_client_id()
client_secret = client.get_client_secret()

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)


class Song():

    def __init__(self, title):
        self.title = title
        self.id = self.__get_id()

    def __get_id(self):
        """ Get the FullTrack class that contains everything """
        return spotify.search(self.title, types=('track',))[0]

    def names(self):
        """ return the list of names that the client found from the search """
        return [item.name for item in self.id.items]

    def length(self):
        """ return the len of the song, by minutes and seconds """
        pass

    def cover(self):
        """ returns a list of URLs of album covers that contains the searched song (similar items also - not a specific track) """
        return [item.album.images[0].url for item in self.id.items]

    def artist(self):
        """ return a list of artists for the song that was searched (similar items also - not a specific track)  """
        return [item.artists[0].name for item in self.id.items]

    def album(self):
        """ returns a list of names of albums that contain the song and similar song also (similar items also - not a specific song) """
        return [item.album.name for item in self.id.items]

    def link(self):
        """ returns the link of the spotify song """
        pass

    def preview_url(self):
        """ return a list of previews for all the songs that similar to the searched song """
        return [item.preview_url for item in self.id.items]

    def release_date(self):
        """ returns the publish date of the song """
        pass
