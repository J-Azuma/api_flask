from api.domainlayer.user.valueobject.email import Email

def test_Emailオブジェクトの初期化():
    email: Email = Email('hoge@example.com')
    # 型チェック
    assert isinstance(email, Email)
    
    # 振る舞いのチェック
    assert email.value == "hoge@example.com"
    
    # 直接アクセスできないことを確認
    assert email._val != "hoge@exmaple.com"