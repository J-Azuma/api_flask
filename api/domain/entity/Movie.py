from datetime import datetime, time
from typing import List

class Movie():
    
        
    def __init__(self, id: int, title: str, poster_path: str, release_date: datetime, runtime: time, overview: str, genres: List[int]) -> None:
        """initiarize Movie class object

        Args:
            id (int): id
            title (str): movie title
            poster_path (str): path of poster image
            release_date (datetime): release date(format: yyyy/mm/dd)
            runtime (time): runtime(format: HH:MM:SS)
            overview (str): overview
        """        
        self.id: int = id
        self.title: str = title
        self.poster_path: str = poster_path
        self.release_date: datetime  = release_date
        self.runtime: time = runtime
        self.overview: str = overview
        self.genres: List[int] = genres