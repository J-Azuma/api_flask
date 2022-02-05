from datetime import date
from api.domainlayer.movie.Movie import Movie

class MovieData():
    """Movieクラスのインスタンスを変換する。 プレゼンテーション層からドメインオブジェクトを隠蔽することが目的。
       責務上、Movieクラスのドメインオブジェクトが渡されることが確定しているので、値チェックは実装しない
    """    
    def __init__(self, movie: Movie) -> None:
        """オブジェクトを初期化

        Args:
            movie (Movie): Movieクラスのドメインオブジェクト
        """        
        self.id: int = movie.id
        self.title: str = movie.title
        self.poster_path: str = movie.poster_path
        self.release_date: str = movie.release_date.strftime('%Y-%m-%d')
        self.runtime: int = movie.runtime
        self.overview: str = movie.overview
        self.genres: list = movie.genres