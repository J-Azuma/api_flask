from api.domainlayer.password.password import Password
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email

def createuser() -> User:
    """テスト用Userクラスインスタンスを生成

    Returns:
        User: Userクラスインスタンス
    """    
    user: User = User(Email("hoge@example.com"), False)
    return user

def createpassword(id: str):
    """Passwordクラスインスタンスを生成

    Args:
        id (str): Userid

    Returns:
        _type_: Passwordクラスインスタンス
    """    
    password: Password = Password(id, "hoge_25252525")
    return password