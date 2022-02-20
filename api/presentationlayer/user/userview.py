import json
from urllib import request
from flask import Blueprint, jsonify
from cerberus import Validator

from api.presentationlayer.shared.validation.japaneseerrorhandler import JapaneseErrorHandler
class UserView():
    
    user_route = Blueprint('user_route' , __name__)
    
    @user_route.route('' , methods=['POST'])
    def create():
        
        param: dict = json.loads(request.json)
        
        v = Validator(create_schema, error_handler = JapaneseErrorHandler)
        if not v.validate({'email': param['email'] , 'password' : param['password']}):
            return jsonify({'result' : 'failure', 'errors' : v.errors}), 400
        