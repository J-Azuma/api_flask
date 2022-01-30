
from typing import ClassVar
from flask import Blueprint, jsonify, make_response
import json

from api.domainlayer.movie.Imovierepository import ImovieRepository
from api.infrastructurelayer.movie.movierepository import MovieRepository
from api.presentationlayer.movie.encoder import Encoder
from api.usecaselayer.movies.moviedetail import MovieDetail
from api.usecaselayer.movies.moviedata import MovieData


class MovieView(object):
    
    movie_route: ClassVar[Blueprint] = Blueprint('movie_route', __name__)
    
    
    @movie_route.route('<int:id>' , methods=['GET'])
    def get_by_id(id: int):
        
        movierepository: ImovieRepository = MovieRepository()
        
        findmoviebyid: MovieDetail = MovieDetail(movierepository)
        movie_data: MovieData = findmoviebyid.show(id)
                
        return make_response(jsonify({
            'code' : 200,
            'movie': json.dumps(movie_data, cls=Encoder, ensure_ascii=False)
        }), 200)
        
        
        
        