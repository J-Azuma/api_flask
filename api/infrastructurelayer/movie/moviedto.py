from datetime import datetime, time, date
from api.domainlayer.movie.Movie import Movie

class MovieDto():
    """MovieReposirotyから取得したdictをMovieクラスのエンティティに詰め替える
       やや冗長だが、リポジトリの可読性向上のため作成。エンティティからdictへの詰め替えは実装しない
    """        
    def __init__(self, params: dict):
        """初期化 例外が発生するケースがいまいち分からん。 TMDBAPIからのみ値を取得するので不正な値は一旦考慮しない

        Args:
            params (dict): TMDBAPIから取得したデータ
        """        
        
        self.id: int = params["id"]
        self.title: str  = params["title"]
        self.poster_path: str  = params["poster_path"]
        self.release_date: date = date.fromisoformat(params["release_date"])
        self.runtime: int = int(params["runtime"])
        self.overview: str = params["overview"]
        self.genres: list[int] = params["genres"]
    
    
    def convert_to_entity(self) -> Movie:
        """DTOをMovieクラスのエンティティに変換

        Returns:
            Movie: Movieクラスのエンティティ
        """       
        movie: Movie = Movie(
            self.id,
            self.title,
            self.poster_path,
            self.release_date,
            self.runtime,
            self.overview,
            self.genres
        )
        return movie