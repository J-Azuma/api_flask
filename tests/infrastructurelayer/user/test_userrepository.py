from distutils.command.clean import clean
from imghdr import tests
from typing import Union
from api.infrastructurelayer.user.userrepository import UserRepository
from api.domainlayer.user.user import User
from tests.common.factory import createuser


def test_User登録(client):
    
        user: User = createuser()
        userrepository = UserRepository()
        # 操作： user登録登録したユーザを検索
        userrepository.add(user)
        registerd_user: Union[User, None] = userrepository.find_by_id(user.id)
        
        # 想定結果
        assert isinstance(registerd_user, User)
        assert registerd_user.id == user.id
        assert registerd_user.email == user.email
        assert registerd_user.is_verified == user.is_verified
    
    