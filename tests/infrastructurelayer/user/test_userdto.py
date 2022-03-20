from ulid import ULID
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email
from api.infrastructurelayer.user.userdto import UserDto
from tests.common.factory import createuser

def test_新規作成したUserインスタンスをDTOに変換():
    # 事前準備： Userインスタンス新規作成
    user: User = createuser()
    
    # 操作： DTOに変換
    userdto = UserDto.from_entity(user)
    
    # 想定結果
    assert isinstance(userdto, UserDto)
    assert userdto.id == user.id
    assert userdto.email == "hoge@example.com"
    assert userdto.is_verified == False


def test_再構成したUserインスタンスをDTOに変換_1():
    
    # 事前準備： Userインスタンスを再構成
    id: str = str(ULID())
    user: User = User(id, Email("hoge@example.com") , False)
    
    # 操作： DTOに変換
    userdto: UserDto = UserDto.from_entity(user)
    
    # 想定結果
    assert isinstance(userdto, UserDto)
    assert userdto.id == id
    assert userdto.email == "hoge@example.com"
    assert userdto.is_verified == False
    
def test_再構成したUserインスタンスをDTOに変換_2():
    
    # 事前準備： Userインスタンスを再構成
    id = str(ULID())
    user: User = User(id, Email("hoge@example.com") , True)
    
    # 操作： DTOに変換
    userdto: UserDto = UserDto.from_entity(user)
    
    # 想定結果
    assert isinstance(userdto, UserDto)
    assert userdto.id == id
    assert userdto.email == "hoge@example.com"
    assert userdto.is_verified == True

def test_再構成したDTOをインスタンスに変換_1():
    
    # 事前準備: UserDTOを再構成
    id = str(ULID())
    userdto: UserDto = UserDto(id=id, email="hoge@example.com" , is_verified=False)
    
    # 操作：インスタンスに変換
    user: User = userdto.to_entity()
    
    # 想定結果
    assert isinstance(user, User)
    assert user.id == id
    assert user.email == "hoge@example.com"
    assert user.is_verified == False
    
def test_再構成したDTOをインスタンスに変換_2():
    
    # 事前準備: UserDTOを再構成
    id = str(ULID())
    userdto: UserDto = UserDto(id=id, email="hoge@example.com" , is_verified=True)
    
    # 操作：インスタンスに変換
    user: User = userdto.to_entity()
    
    # 想定結果
    assert isinstance(user, User)
    assert user.id == id
    assert user.email == "hoge@example.com"
    assert user.is_verified == True