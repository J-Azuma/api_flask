from flask import (Blueprint, jsonify)

bp = Blueprint('hello' , __name__ , url_prefix='/hello' );

@bp.route('', methods=['GET'])
def hello():
    return jsonify(
      {
        'code' : 200,
        'response' : 'Hello, World!'
      }
    )