
from webbrowser import get
from api.domainlayer.movie.Imovierepository import ImovieRepository
from api.domainlayer.movie.Movie import Movie
from api.infrastructurelayer.movie.moviedto import MovieDto
from api.infrastructurelayer.movie.movierepository import MovieRepository
from api.usecaselayer.movies.moviedata import MovieData


class MovieDetail():
    
    def __init__(self, movierepository: ImovieRepository):
        self.movierepository: ImovieRepository = movierepository
    
    
    def show(self, id: int) -> MovieData:
        return self.get(id)
        
    
    def get(self, id: int) -> MovieData:
        movierepository: ImovieRepository = self.movierepository
        movie: Movie = movierepository.find_by_id(id)
        return MovieData(movie)