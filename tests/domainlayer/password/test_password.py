
from ast import Pass
from pytest import raises
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email
from api.domainlayer.password.password import Password
from api.presentationlayer.shared.exception.exceptionhandler import BadRequestException

def test_Passwordオブジェクト生成():
    # 事前条件： Userオブジェクト生成
    user: User = User(Email("hoge@example.com"))
    
    # 事前条件：パスワード文字列
    passwordstr: str = "Azuma_5050"
    
    # Passwordオブジェクト生成
    password: Password = Password(user.id, passwordstr)
    
    # 型確認
    assert isinstance(password, Password)
    
    # useridとpasswordidが一致する
    assert user.id == password.user_id
    
    # パスワードの値確認
    assert password.value == "Azuma_5050"

def test_IDの値が不正な場合に例外を出す():
    
    with raises(BadRequestException) as e:
        password: Password = Password("1", "Azuma_5050")
    
    assert str(e.value) == "ユーザIDの値が不正です。"

def test_passwordの値変更():
    
    # 事前条件：Passwordオブジェクト生成
    user: User = User(Email("hoge@example.com"))
    password: Password = Password(user.id, "Azuma_5050")
    
    # 変更前の値
    assert password.value == "Azuma_5050"
    
    # 変更後の値
    password.change("Azuma_3939")
    assert password.value == "Azuma_3939"
    assert password.value != "Azuma_5050"