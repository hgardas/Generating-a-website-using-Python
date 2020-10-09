# Movie Class with 4 variables
class Movie():
    """ This is the Movie class """
    def __init__(self, title, franchise,
                 poster_image_url, trailer_youtube_url):
        """ This function is called
            when an instance of the Movie class is called """
        self.title = title
        self.franchise = franchise
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
