from unittest import mock

import pytest
from api.domainlayer.shared.domainexception import BadRequestDomainException

from api.domainlayer.user.service.validateuser import ValidateUser
from api.config.dependency import Dependency
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.infrastructurelayer.user.userrepository import UserRepository
from api.domainlayer.user.user import User
from tests.common.factory import createuser

def test_DIコンテナでインスタンス生成():
    # 事前条件： なし
    
    # 操作： Dependency経由でvalidateuserインスタンスを生成
    dependency: Dependency = Dependency()
    validate_user: ValidateUser = dependency.resolve(ValidateUser)
    
    # インスタンスが生成されていることを検証
    assert isinstance(validate_user, ValidateUser)
    
    # インスタンスの属性を検証
    assert hasattr(validate_user, 'userrepository')
    assert isinstance(validate_user.userrepository, IuserRepository)

def test_exists関数_ユーザが重複する(mocker):
    # 事前条件： なし
    
    # 操作： validateuserインスタンスを生成
    user: User = createuser()
    userrepository: IuserRepository = UserRepository()
    mocker.patch.object(userrepository, 'find_by_email' , return_value=user)
    validate_user: ValidateUser = ValidateUser(userrepository)
    
    
    exists_user: bool = validate_user.exists(user)
    
    # 重複あり
    assert exists_user == True

def test_exists関数_ユーザが重複しない(mocker):
    # 事前条件： なし
    
    # 操作： validateuserインスタンスを生成
    user: User = createuser()
    userrepository: IuserRepository = UserRepository()
    mocker.patch.object(userrepository, 'find_by_email' , return_value=None)
    validate_user: ValidateUser = ValidateUser(userrepository)
    
    
    exists_user: bool = validate_user.exists(user)
    
    # 重複がないことを検証
    assert exists_user == False

def test_ユーザ重複時に例外を送出(mocker):
    # 事前条件： なし
    
    # 操作： validateメソッドを呼び出し
    user = createuser()
    dependency = Dependency()
    validate_user: ValidateUser = dependency.resolve(ValidateUser)
    
    mocker.patch.object(validate_user, 'exists' , return_value=True)
    with pytest.raises(BadRequestDomainException) as e:
        validate_user.validate(user)
    
    assert str(e.value) == "メールアドレスが重複しています"

def test_ユーザのメールアドレスが重複しない場合何もしない(mocker):
    # 事前条件： なし
    
    # 操作： validateメソッドを呼び出し
    user = createuser()
    dependency = Dependency()
    validate_user: ValidateUser = dependency.resolve(ValidateUser)
    
    mocker.patch.object(validate_user, 'exists' , return_value=False)
    validate_user.validate(user)
    
    assert True