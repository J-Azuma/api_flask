from datetime import date, datetime, time
from typing import List

class Movie():
    
        
    def __init__(self, id: int, title: str, poster_path: str, release_date: date, runtime: int, overview: str, genres: List) -> None:
        """initiarize Movie class object

        Args:
            id (int): id
            title (str): movie title
            poster_path (str): path of poster image
            release_date (datetime): release date(format: Y-m-d)
            runtime (time): runtime(format: HH:MM:SS)
            overview (str): overview
            genres (List[int]): genres of movie
        """        
        self.id: int = id
        self.title: str = title
        self.poster_path: str = poster_path
        self.release_date: date  = release_date
        self.runtime: int = runtime
        self.overview: str = overview
        self.genres: list = genres