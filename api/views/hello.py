from flask import (Blueprint, jsonify)
from flask_jwt import jwt_required

bp = Blueprint('hello' , __name__ , url_prefix='/hello' );

@bp.route('', methods=['GET'])
@jwt_required()
def hello():
    return jsonify(
      {
        'code' : 200,
        'response' : 'Hello, World!'
      }
    )