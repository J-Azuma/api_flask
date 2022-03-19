from http.client import BAD_REQUEST
import pytest

def test_emailが空文字(client):
    # 前提条件： 無し
    
    # 操作： emailが空文字のリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"email": "" , "password" :"user01password"},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコードと形式
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object: dict = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "email" in res_object["errors"]
    assert isinstance(res_object["errors"]["email"], list)
    assert res_object["errors"]["email"][0] == "emailは必須項目です"

def test_emailが渡されない(client):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"password" :"user01password"},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "email" in res_object["errors"]
    assert isinstance(res_object["errors"]["email"], list)
    assert res_object["errors"]["email"][0] == "必須項目です"


@pytest.mark.parametrize('param', [
                         {'email' : 1, 'password' : 'hogehoge_2525'},
                         {'email' : 0, 'password' : 'hogehoge_2525'},
                         {'email' : 2.5, 'password' : 'hogehoge_2525'}])
def test_emailが文字列以外(client, param):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json=param,  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "email" in res_object["errors"]
    assert isinstance(res_object["errors"]["email"], list)
    assert res_object["errors"]["email"][0] == "string型で入力してください。"
    
@pytest.mark.parametrize('param', [
                         {'email' : 'aaaaaa', 'password' : 'hogehoge_2525'},
                         {'email' : 'hogehoge_com', 'password' : 'hogehoge_2525'},
                         {'email' : 'test@aaaa_com', 'password' : 'hogehoge_2525'}])
def test_emailの形式が不正(client, param):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json=param,  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "email" in res_object["errors"]
    assert isinstance(res_object["errors"]["email"], list)
    assert res_object["errors"]["email"][0] == "値が不正です"

def test_passwordが空文字(client):
    # 前提条件： 無し
    
    # 操作： emailが空文字のリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"email": "hoge@example.com" , "password" :""},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコードと形式
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object: dict = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "password" in res_object["errors"]
    assert isinstance(res_object["errors"]["password"], list)
    assert res_object["errors"]["password"][0] == "passwordは必須項目です"


def test_passwordが渡されない(client):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"email" :"hoge@example.com"},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "password" in res_object["errors"]
    assert isinstance(res_object["errors"]["password"], list)
    assert res_object["errors"]["password"][0] == "必須項目です"
    
def test_passwordが8文字未満(client):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"email" : "hoge@example.com", "password" : "Azuma_1"},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "password" in res_object["errors"]
    assert isinstance(res_object["errors"]["password"], list)
    assert res_object["errors"]["password"][0] == "passwordは8文字以上で入力してください"

def test_passwordが31文字以上(client):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json={"email" : "hoge@example.com", "password" : "Azuma_1aaaaaaaaaaaaaaaaaaaaaaaa"},  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "password" in res_object["errors"]
    assert isinstance(res_object["errors"]["password"], list)
    assert res_object["errors"]["password"][0] == "passwordは30文字以内で入力してください"

@pytest.mark.parametrize('param', [
                         {'email' : 'hoge@example.com', 'password' : 'aaaaaaaa'}, # 1. 小文字
                         {'email' : 'hoge@example.com', 'password' : 'AAAAAAAA'}, # 2. 大文字,
                         {'email' : 'hoge@example.com', 'password' : 'aAaAaAaAaA'}, # 3. 小文字大文字
                         {'email' : 'hoge@example.com', 'password' : '11111111'}, # 4. 数字
                         {'email' : 'hoge@example.com', 'password' : '---------'}, # 5. 記号
                         {'email' : 'hoge@example.com', 'password' : 'a-a-a-a-a-a-'}, # 6. 小文字と記号
                         {'email' : 'hoge@example.com', 'password' : 'A-A-A-A-'}, # 7. 大文字と記号
                         {'email' : 'hoge@example.com', 'password' : 'a1a1a1a1'}, # 8. 小文字と数字
                         {'email' : 'hoge@example.com', 'password' : 'A1A1A1A1'}, # 9. 大文字と数字
                         {'email' : 'hoge@example.com', 'password' : '-1-1-1-1-1'}, # 10. 数字と記号
                         {'email' : 'hoge@example.com', 'password' : 'aA------'}, # 12. 小文字と大文字と記号
                         {'email' : 'hoge@example.com', 'password' : 'a1------'}, # 13. 小文字と数字と記号
                         {'email' : 'hoge@example.com', 'password' : 'A1------'}, # 14. 小文字と大文字と記号
                         {'email' : 'hoge@example.com', 'password' : 'ああああああああ'}, # . 平仮名
                         {'email' : 'hoge@example.com', 'password' : 'スリジャヤワルダナプラコッテ'}, # . 片仮名
                         {'email' : 'hoge@example.com', 'password' : '鹿児島県志布志市志布志'} # . 漢字
                         ])
def test_passwordの形式が不正(client, param):
    # 前提条件： なし
    
    # 操作： emailが設定されていないリクエストデータを送信
    response = client.post('/api/v1/users/' , json=param,  headers={"Content-Type" : "application/json"})
    
    # 想定結果： レスポンスのステータスコード
    assert response.status_code == BAD_REQUEST
    assert response.headers['content-type'] == 'application/json'
    
    # 想定結果： レスポンスの内容
    res_object = response.get_json()
    assert isinstance(res_object, dict)
    
    assert isinstance(res_object["result"], str)
    assert res_object["result"] == "failure"
    
    assert isinstance(res_object["errors"], dict)
    assert "password" in res_object["errors"]
    assert isinstance(res_object["errors"]["password"], list)
    assert res_object["errors"]["password"][0] == "値が不正です"