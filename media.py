import webbrowser

class Movie:
    """
    This class represents a Movie with basic information
    """

    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
