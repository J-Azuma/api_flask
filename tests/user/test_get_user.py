from flask import request, jsonify
def test_getUserList(client):
    response = client.get('/api/user/list').get_json()
    assert response is not None
    assert response['code'] == 200
    assert response['users'][0]['uid'] == 1
    assert response['users'][0]['username'] == 'user1'