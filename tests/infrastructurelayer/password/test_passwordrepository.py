from werkzeug.security import  check_password_hash
from api.domainlayer.user.user import User
from api.domainlayer.password.password import Password
from api.infrastructurelayer.password.passwordrepository import PasswordRepository
from api.infrastructurelayer.user.userrepository import UserRepository
from tests.common.factory import createpassword, createuser
from api.infrastructurelayer.database import session

def test_Password登録():
    
    # 事前条件：UserインスタンスをDBに登録する(テスト用データ作成メソッドでユーザ作成・ユーザ登録は別々にすべき？)
    user: User = createuser()
    userrepository = UserRepository()
    userrepository.add(user)
    session.commit()
    
    # 操作： パスワードインスタンスをDBに登録する
    password: Password = createpassword(user.id)
    passwordrepository = PasswordRepository()
    passwordrepository.add(password)
    session.commit()
    
    # 想定結果： パスワードがDBに登録されている
    password: Password = passwordrepository.find(user.id)
    
    assert isinstance(password, Password)
    assert password.user_id == user.id
    assert check_password_hash(password.value, "Hoge_25252525")
    
    