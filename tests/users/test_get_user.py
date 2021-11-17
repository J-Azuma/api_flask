from flask import request, jsonify
def test_getUserList(client):
    response = client.get('/api/vi/users/list')
    assert response.status_code == 200

    res_json = response.get_json()
    assert res_json['code'] == 200
    assert res_json['users'][0]['uid'] == 1
    assert res_json['users'][0]['username'] == 'user1'