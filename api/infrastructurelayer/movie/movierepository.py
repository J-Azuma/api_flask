import json
import typing
from flask import current_app
import requests
from api.domainlayer.movie.Movie import Movie
from api.infrastructurelayer.movie.moviedto import MovieDto
from ...domainlayer.movie.Imovierepository import ImovieRepository

class MovieRepository(ImovieRepository):
    """TMDBAPIから映画のデータを取得する。

    Args:
        ImovieRepository ([type]): [description]
    """    
    def __init__(self):
        self.__token: str = current_app.config["TOKEN"]
        self.__headers = {'Content-Type' :'application/json:charset=utf-8'}
        self.__base_url: str = current_app.config["BASE_URL"]
        self.__base_image_url: str = current_app.config["BASE_IMAGE_URL"]
        self.__quert_string: str = f'?language=ja-JP&api_key={self.__token}'
        
    def find_by_id(self, id: int) -> Movie:
        url = f'{self.__base_url}movie/{id}{self.__quert_string}'

        dict_data: dict = self.get_json_data(url)
        movie_dto = MovieDto(dict_data)
        
        return movie_dto.convert_to_entity()
    
    def findby_name(self, name: str):
        pass
    
    def get_json_data(self, url: str, params: dict={}) -> dict:
        res = requests.get(url, headers=self.__headers, params=params)
        dict_data: dict = json.loads(res.text)
        return dict_data