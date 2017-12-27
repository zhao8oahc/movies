import webbrowser


class Movie():
    """This class provides a way to store movie related information

        Args:
            movie_title -- string
            movie_storyline -- string
            poster_image -- string(url)
            trailer_youtube -- string(url)
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Form movie instances."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
