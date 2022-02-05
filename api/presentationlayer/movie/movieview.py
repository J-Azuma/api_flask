
from typing import ClassVar

from flask import Blueprint, jsonify, make_response
import json
from cerberus import Validator

from api.domainlayer.movie.Imovierepository import ImovieRepository
from api.infrastructurelayer.movie.movierepository import MovieRepository
# プレゼンテーション層がドメイン層とインフラ層に依存している。何とかしたい
from api.presentationlayer.movie.validation.schema import get_by_id_schema
from api.presentationlayer.shared.validation.japaneseerrorhandler import  JapaneseErrorHandler
from api.usecaselayer.movies.moviedetail import MovieDetail
from api.usecaselayer.movies.moviedata import MovieData


class MovieView(object):
    """映画情報を取得するエンドポイント

    Args:
        object ([type]): [description]

    Returns:
        [type]: TMDBAPIから取得した映画情報をjson形式で返す
    """    
    movie_route: ClassVar[Blueprint] = Blueprint('movie_route', __name__)
    
    
    @movie_route.route('<int:id>' , methods=['GET'])
    def get_by_id(id: int):
        """idで映画を検索

        Args:
            id (int): 映画のID

        Returns:
            [type]: 指定したIDの映画情報
        """        
        v = Validator(get_by_id_schema, error_handler = JapaneseErrorHandler)
        if not v.validate({'id' : id}):
            return jsonify({'result' : 'failure' , 'id' : id, 'errors' : v.errors}), 400
        
        
        movierepository: ImovieRepository = MovieRepository()
        
        findmoviebyid: MovieDetail = MovieDetail(movierepository)
        movie_data: MovieData = findmoviebyid.show(id)
                
        return jsonify({
            'code' : 200,
            'movie': movie_data.__dict__
        }), 200
        
        
        
        