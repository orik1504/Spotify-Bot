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


class Song():

    def __init__(self, title):
        self.title = title

    def length(self):
        """ return the len of the song, by minutes and seconds """
        pass

    def cover(self):
        """ returns the cover of the song, a picture """
        pass

    def artist(self):
        """ returns an artist instance (can get a name, more albums...) """
        pass

    def album(self):
        """ returns the album that the song is published with """
        pass

    def link(self):
        """ returns the link of the spotify song """
        pass

    def publish_time(self):
        """ returns the publish date of the song """
        pass
