from api.domainlayer.movie.Movie import Movie
from ..domainlayer.movie.Imovierepository import ImovieReposirtory

class MovieRepository(ImovieReposirtory):
    
    def __init__(self, token):
    