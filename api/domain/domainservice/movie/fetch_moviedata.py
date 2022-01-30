import requests
import json
from pprint import pprint

class FetchMovieData():
    
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers_ = {'Authorization' : f'Bearer {self.token}' , 'Content-Type' :'application/json:charset=utf-8'}
        self.base_url_ = 'https://api.themoviedb.org/3/'
        self.img_base_url_ = 'https://image.tmdb.org/t/p/w500'
    
    def _json_by_get_request(self, url: str, params: dict = {}):
        """convert json to Python object

        Args:
            url (str): endpoint to which send request
            params (dict, optional): request parameter. Defaults to {}.

        Returns:
            obj: movie data
        """                
        res = requests.get(url, headers=self.headers_, params=params)
        return json.loads(res.text)
    
    def search_movie(self, query):
        params = {'query' : query}
        url = f'{self.base_url_}search/movie'
        return self._json_by_get_request(url, params)
    
    def get_movie(self, movie_id):
        url = f'{self.base_url_}movie/{movie_id}'
        return self._json_by_get_request(url)
    
    def get_genres(self):
        url = f'{self.base_url_}genre/movie/list'
        return self._json_by_get_request(url)
    
token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZDgyZmExZWQ1Njc3YThjMGQ4ZGU1NzExZDAxMWM2YSIsInN1YiI6IjYxNzNiOGNmNWM1Y2M4MDA5MzJmNmEzYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.t0ZaV0zRGYxFhnqr6ohfoyT1b5JeRNV8dF-69SBKsOU"
movie: FetchMovieData = FetchMovieData(token)
res = movie.get_movie(2)
pprint(res)