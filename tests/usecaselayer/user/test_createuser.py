from unittest import mock
import pytest
from api.config.dependency import Dependency
from api.domainlayer.user.service.validateuser import ValidateUser
from api.infrastructurelayer.password.passwordrepository import PasswordRepository
from api.infrastructurelayer.user.userrepository import UserRepository
from api.usecaselayer.user.createuser import CreateUser
from api.domainlayer.shared.domainexception import BadRequestDomainException

def test_DIコンテナでCreateUserインスタンス作成():
    # 事前条件： なし
    
    # 操作：DIコンテナ経由でインスタンス作成
    dependency: Dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    # 想定結果： インスタンスが正常に生成されること
    assert isinstance(createuser, CreateUser)
    
    assert hasattr(createuser, 'userrepository')
    assert isinstance(createuser.userrepository, UserRepository)
    
    assert hasattr(createuser, 'validateuser')
    assert isinstance(createuser.validateuser, ValidateUser)
    
    assert hasattr(createuser, 'passwordrepository')
    assert isinstance(createuser.passwordrepository, PasswordRepository)
    
    
def test_メールアドレスとパスワードをリポジトリに渡す_異常系(mocker):
    # 操作：DIコンテナ経由でインスタンス作成
    dependency: Dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    mocker.patch.object(createuser.validateuser, 'exists' , return_value=True)
    
    param: dict = {
        'email' : 'hoge@exmaple.com',
        'password' : 'hoge_25252525'
    }
    with pytest.raises(BadRequestDomainException) as e:
        createuser.register(param)
    
    assert str(e.value) == "メールアドレスが重複しています"
        
def test_メールアドレスとパスワードをリポジトリに渡す_正常系(mocker):
    # 事前準備
    
    # ユースケースのインスタンスを作成
    dependency: Dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    # リポジトリとサービスをモック化
    user_repository_add_mock = mock.Mock()
    password_repository_add_mock = mock.Mock()
    mocker.patch.object(createuser.validateuser, 'exists' , return_value=False)
    mocker.patch.object(createuser.userrepository, 'add', side_effect=user_repository_add_mock)
    mocker.patch.object(createuser.passwordrepository, 'add', side_effect=password_repository_add_mock)
    
    # 操作： メールアドレスとパスワードをregisterメソッドに渡す
    param: dict = {
        'email' : 'hoge@exmaple.com',
        'password' : 'hoge_25252525'
    }
    createuser.register(param)
    
    # 検証： リポジトリが呼び出されたことを検証
    user_repository_add_mock.assert_called_once()
    password_repository_add_mock.assert_called_once()
    
    # 引数を検証したいが...