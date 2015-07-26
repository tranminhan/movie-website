import tmdbsimple as tmdb
import fresh_tomatoes
import media

# the API Key to query movie data at https://www.themoviedb.org
tmdb.API_KEY = '31aa58f2cdafa6a8d0e729b21b2a523f'


def query_top_rated_movies():
    """Fetch top-rated movies from https://www.themoviedb.org

        Movie information includes title, storyline, poster, youtube trailer and rating

        return: list of top-rated Movies objects
    """
    movies = []

    # the tmdbsimple api to query top-rated movies
    top_rated_movies = tmdb.Movies().top_rated(page=1, language='en')
    for movie in top_rated_movies['results']:
        videos = tmdb.Movies(movie['id']).videos()['results']

        # only looking for movies with trailers
        if len(videos) > 0:
            video = videos[0]

            movies.append(
                media.Movie(
                    movie['title'],
                    movie['overview'],
                    u'https://image.tmdb.org/t/p/w300/' + movie['poster_path'],
                    u'https://www.youtube.com/watch?v=' + video['key'],
                    str(movie['vote_average'])
                )
            )

    return movies


fresh_tomatoes.open_movies_page(query_top_rated_movies())
