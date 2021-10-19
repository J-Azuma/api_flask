from flask import request, jsonify


def test_hello(client):
  response = client.get('/hello/')
  res_json = response.get_json()
  assert response.status_code == 200
  assert res_json['response'] == 'Hello, World!'

    