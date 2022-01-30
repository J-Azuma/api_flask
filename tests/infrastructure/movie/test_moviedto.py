from datetime import date, time
from typing import Dict
from api.infrastructurelayer.movie.moviedto import MovieDto


def test_オブジェクト生成():
    """dtoが正常に作成されることをテスト
    """    
    movie_dto: MovieDto = MovieDto(data())
    # インスタンスのクラス確認
    assert isinstance(movie_dto, MovieDto) is True
    
    # プロパティの値と型を確認
    assert movie_dto.id == 2
    assert isinstance(movie_dto.id, int)
    
    assert movie_dto.title == "ファイトクラブ"
    assert isinstance(movie_dto.title, str)
    
    assert movie_dto.poster_path == "123456789.jpg"
    assert isinstance(movie_dto.poster_path, str)
    
    assert movie_dto.release_date == date(1999, 12,11)
    assert isinstance(movie_dto.release_date, date)
    
    assert movie_dto.runtime == 139
    assert isinstance(movie_dto.runtime , int)
    
    assert movie_dto.overview == "fugafuga"
    assert isinstance(movie_dto.overview, str)
    
    assert movie_dto.genres == [1 , 4]
    assert isinstance(movie_dto.genres , list)
    
     

def data() -> dict:
    """テスト用のdictオブジェクト生成

    Returns:
        dict: DTOに変換するdictオブジェクト
    """    
    dict: Dict = {
        "id" : 2,
        "title": "ファイトクラブ",
        "poster_path": "123456789.jpg",
        "release_date": "1999-12-11",
        "runtime": "139",
        "overview": "fugafuga",
        "genres" : [
            1,
            4
        ]
    }
    return dict