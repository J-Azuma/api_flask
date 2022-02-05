


def test_get_by_idの正常系(client):
    response = client.get('/api/v1/movies/2')
    # HTTP形式の確認
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    
    # レスポンスの中身の確認
    res_json = response.get_json()
    assert isinstance(res_json, dict)
    
    assert res_json["code"] == 200
    assert isinstance(res_json["movie"], dict)
    
    assert isinstance(res_json["movie"]["id"], int)
    assert res_json["movie"]["id"] == 2
    
    assert isinstance(res_json["movie"]["title"] , str)
    assert res_json["movie"]["title"] == "Ariel"
    
    assert isinstance(res_json["movie"]["release_date"], str)
    assert res_json["movie"]["release_date"] == "1988-10-21"
    
    assert isinstance(res_json["movie"]["runtime"], int)
    assert res_json["movie"]["runtime"] == 73
    
    assert isinstance(res_json["movie"]["overview"], str)
    assert res_json["movie"]["overview"] == ""
    
    assert isinstance(res_json["movie"]["poster_path"], str)
    assert res_json["movie"]["poster_path"] == "/ojDg0PGvs6R9xYFodRct2kdI6wC.jpg"