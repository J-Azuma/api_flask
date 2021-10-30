from flask import Blueprint, request, make_response, jsonify
from api.models.user import User, UserSchema
import json

user_route = Blueprint('user_route' , __name__)

@user_route.route('/user/list', methods=['GET'])
def getUsers():
    
    users: list = User.getUserList()
    user_schema: UserSchema = UserSchema(many=True)

    return make_response(jsonify({
      'code': 200,
      'users': user_schema.dump(users)
    }), 200)
    