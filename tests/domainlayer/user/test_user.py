from time import sleep

from ulid import ULID
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email

def test_Userエンティティの初期化():
    id: str = str(ULID())
    email: Email = Email("hoge@example.com")
    user: User = User(id, email)
    
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
    id1: str = str(ULID())
    user1 = User(id1, Email("fuga@exmaple.com"))
    
    id2: str = str(ULID())
    user2 = User(id2, Email("fizz@exmaple.com"))
    
    # IDが異なることを確認
    assert user1.id != user2.id

def test_UserIDが辞書順になることを確認():
    # 事前条件： Userインスタンスを2つ作成
    id1: str = str(ULID())
    user1 = User(id1, Email("fuga@exmaple.com"))
    
    sleep(0.1)
    id2: str = str(ULID())
    user2 = User(id2, Email("fizz@exmaple.com"))
    
    # user2のidが大きいことを確認
    assert user1.id < user2.id

def test_有効化状態でインスタンスを生成():
    id: str = str(ULID())
    user = User(id, Email("fuga@exmaple.com"), True)
    
    # is_verifyがTrueである
    assert user.is_verified == True
    
def test_アカウントの有効化():
    # 事前条件： 初期状態ではis_verifiedがFalse
    id: str = str(ULID())
    user = User(id, Email("fuga@exmaple.com"))
    assert user.is_verified == False 
    
    # 操作： verifyメソッド実行
    user.verify()
    
    # 想定結果： is_verifyがTrueになっている
    assert user.is_verified == True