
from typing import Union
from datetime import date
import json

from api.usecaselayer.movies.moviedata import MovieData

class Encoder(json.JSONEncoder):
    
    def default(self, obj: Union[MovieData, date]):
        if isinstance(obj, date):
            return str(obj)
        if isinstance(obj, MovieData) and hasattr(obj, '__dict__'):
            return obj.__dict__
        
        return json.JSONEncoder.default(self, obj)