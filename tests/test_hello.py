from flask import json, request, jsonify


def test_hello(client):
    response = client.get('/hello').get_json()
    assert response['code'] == 200
    assert response['response'] == 'Hello, World!'

    