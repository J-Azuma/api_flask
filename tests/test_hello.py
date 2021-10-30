from flask import json, request, jsonify


def test_hello(client):
    response = client.get('/hello')
    assert response.status_code== 200
    res_json = response.get_json()
    assert res_json['code'] == 200
    assert res_json['response'] == 'Hello, World!'

    