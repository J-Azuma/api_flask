
from ulid import ULID

from api.domainlayer.password.password import Password
from api.infrastructurelayer.password.passworddto import PasswordDto

def test_新規PasswordインスタンスをDTOに変換():
    # 備考： 新規作成時もidをコンストラクタに渡すので再構成はテストしない
    
    # 事前条件： Passwordインスタンスを作成
    id = str(ULID())
    value = "Azuma_1234"
    password: Password = Password(id, value)
    
    # 操作： DTOに変換
    passworddto: PasswordDto = PasswordDto.from_entity(password)
    
    # 想定結果
    assert isinstance(passworddto, PasswordDto)
    assert passworddto.user_id == id
    assert passworddto.value == "Azuma_1234"

def test_DTOをPasswordインスタンスに変換():
    # 事前条件：DTOを作成
    id = str(ULID())
    value = "Azuma_1234"
    passworddto: PasswordDto = PasswordDto(user_id=id, value=value)
    
    # 操作：エンティティに変換
    password: Password = passworddto.to_entity()
    
    # 想定結果
    assert isinstance(password, Password)
    assert password.user_id == passworddto.user_id
    assert password.value == passworddto.value
    
    
    
    
    