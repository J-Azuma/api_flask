from datetime import date
from api.domainlayer.movie.Movie import Movie

class MovieData():
    
    def __init__(self, movie: Movie) -> None:
        self.id: int = movie.id
        self.title: str = movie.title
        self.poster_path: str = movie.poster_path
        self.release_date: date = movie.release_date
        self.runtime: int = movie.runtime
        self.overview: str = movie.overview
        self.genres: list[int] = movie.genres
        
    