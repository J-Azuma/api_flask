from time import sleep
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email

def test_Userエンティティの初期化():
    email: Email = Email("hoge@example.com")
    user: User = User(email)
    
    # インスタンスが生成されることを確認
    assert isinstance(user,User)
    
    # IDの型確認
    assert isinstance(user.id, str)
    
    # IDの文字数確認
    assert len(user.id) == 26
    
    # メールアドレスの値を確認
    assert user.email == "hoge@example.com"
    assert isinstance(user.email , str)
    
    # is_verifiedの値を確認
    assert isinstance(user.is_verified, bool)
    assert user.is_verified == False
    
def test_UserIDの一意性():
    
    # 事前条件：Userインスタンスを2つ
    user1 = User(Email("fuga@exmaple.com"))
    sleep(0.1)
    user2 = User(Email("fizz@exmaple.com"))
    
    # IDが異なることを確認
    assert user1.id != user2.id

def test_UserIDが辞書順になることを確認():
    # 事前条件： Userインスタンスを2つ作成
    
    user1 = User(Email("fuga@exmaple.com"))
    sleep(0.1)
    user2 = User(Email("fizz@exmaple.com"))
    
    # user2のidが大きいことを確認
    assert user1.id < user2.id

def test_有効化状態でインスタンスを生成():
    user = User(Email("fuga@exmaple.com"), True)
    
    # is_verifyがTrueである
    assert user.is_verified == True
    
def test_アカウントの有効化():
    # 事前条件： 初期状態ではis_verifiedがFalse
    user = User(Email("fuga@exmaple.com"))
    assert user.is_verified == False 
    
    # 操作： verifyメソッド実行
    user.verify()
    
    # 想定結果： is_verifyがTrueになっている
    assert user.is_verified == True