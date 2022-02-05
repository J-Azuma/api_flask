from flask import Blueprint, request, make_response, jsonify
from api.models.user import User, UserSchema
from werkzeug.security import generate_password_hash

class UserView(object):
        
    user_route = Blueprint('user_route' , __name__)

    @user_route.route('', methods=['GET'])
    def getUsers():
        
        users: list = User.getUserList()
        user_schema: UserSchema = UserSchema(many=True)
        
        return make_response(jsonify({
          'code': 200,
          'users': user_schema.dump(users)
        }), 200)


    @user_route.route('', methods=['POST'])
    def createUser():
        user_schema: UserSchema = UserSchema()
        # json形式でパラメータを受け取る
        userData :dict = {
          "email" : request.json['email'] , 
          "password": generate_password_hash(request.json["password"])
        }
        
        user : User = User.registUser(userData)
        
        # レスポンスを返す
        return make_response(jsonify({
          'code': 200,
          'user' : user_schema.dump(user)
        }), 201)

    @user_route.route('verify', methods=['PATCH'])
    def verifyUser():
        uid :int = request.args.get('id')
        User.verifyUser(uid)
        
        return make_response(jsonify({
          'code' : 200,
          'msg' : 'アカウントを有効化しました。'
        }))