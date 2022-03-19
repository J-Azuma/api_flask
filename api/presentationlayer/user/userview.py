from flask import Blueprint, jsonify, request
from cerberus import Validator

from api.presentationlayer.shared.validation.japaneseerrorhandler import JapaneseErrorHandler
from api.presentationlayer.user.validation.schema import create_schema

from api.config.dependency import Dependency
from api.usecaselayer.user.createuser import CreateUser
class UserView():
    
    user_route = Blueprint('user_route' , __name__)
    
    @user_route.route('' , methods=['POST'])
    def create():
        
        param: dict = request.json
        # リクエストパラメータのキーが存在しない場合、そのキーの値をNoneにする→ なんかええ感じの書き方出来そうだが...
        if 'email' not in param:
            param['email'] = None 
        
        if 'password' not in param:
            param['password'] = None
        
        v = Validator(create_schema, error_handler = JapaneseErrorHandler)
       
        if not v.validate({'email': param['email'], 'password' : param['password']}):
            return jsonify({'result' : 'failure', 'errors' : v.errors}), 400
        
        try:
            dependency: Dependency = Dependency()
            create_user: CreateUser = dependency.resolve(CreateUser)
            create_user.register(param)
        except Exception as e:
            raise Exception("ユーザ作成処理に失敗しました")
        
        return jsonify({
            'code' : 200,
            'message' : 'ユーザの仮登録が完了しました。'
        }), 200
        