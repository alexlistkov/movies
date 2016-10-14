import webbrowser


class Movie():
    """ This class provides a way to store movie related information.
        This class includes instances attributes.
        Attributes:
            title: movie title
            storyline: movie storyline
            poster image: link on a poster
            trailer_youtube: youtube link on a trailer
    """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ Inits Movie class with all attributes (title, storyline,
            poster and trailer).
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
