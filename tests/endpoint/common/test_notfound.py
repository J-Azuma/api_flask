
def test_存在しないURLのテスト(client):
    response = client.get('/notfound')
    
    # レスポンス形式のテスト
    assert response.status_code == 404
    assert response.headers['content-type'] == 'application/json'
    
    # レスポンスの中身のテスト
    res_json = response.get_json()
    assert isinstance(res_json, dict)
    
    assert res_json['code'] == 404
    assert res_json['message'] == "指定したリソースがみつかりません。"