from flask import json
from werkzeug.security import generate_password_hash

from api.models.user import User
from api.database import db


def test_createUser(client):
    response = client.post('/api/v1/users/', data=json.dumps({"email": "user01@example.com" , "password" :"user01password"}),  headers={"Content-Type" : "application/json"})
   
    # レスポンスヘッダのテスト
    assert response.status_code == 201
    
    # レスポンスボディのテスト
    res_json = response.get_json()
    assert res_json['code'] == 200
    assert res_json['user']['username'] == ''
    assert res_json['user']['email'] == 'user01@example.com'
    # パスワードのテストどうする？
    #assert res_json['user']['password'] == generate_password_hash('user01password') 
    assert res_json['user']['is_verified'] == 0