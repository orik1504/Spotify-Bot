""" Album class will include: 
* album length (how much songs) + listening time of the album
* Top 5 songs of the album (from songs class , listeners count)
* how much listeners
* album cover (as a picture)
* album artist (as artist class)
* link on spotify
* when the album got out
"""


class Album():

    def __init__(self, title, artist_name):
        self.title = title
        self.artist_name = artist_name

    def len_by_songs(self):
        """ returns how much songs are in the album """
        pass

    def len_by_time(self):
        """ returns the time that takes to a listener to finish the album """
        pass

    def top_5_songs(self):
        """ returns a list of song class instance and returns a name of the song
        the cover of the song, publish date, length of the song, artist name """
        pass

    def listeners(self):
        """ returns the number of people who have listend to the album """
        pass

    def album_cover(self):
        """ returns an album cover """
        pass

    def album_artist(self):
        """ returns the album artist, name, more albums, how much monthly listeners"""
        pass

    def link(self):
        """ returns the album link on spotify """
        pass

    def publish_date(self):
        """ returns a publish date """
        pass
