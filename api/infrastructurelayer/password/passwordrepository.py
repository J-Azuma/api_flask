from werkzeug.security import generate_password_hash

from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.database import db
from api.infrastructurelayer.password.passworddto import PasswordDto

class PasswordRepository(IpasswordRepository):
    
    def __init__(self) -> None:
        self.session = db.session
        
    def add(self, password) -> None:
        """レコードを追加

        Args:
            password (_type_): パスワードインスタンス
        """        
        passworddto: PasswordDto = PasswordDto.from_entity(password)
        passworddto.value = generate_password_hash(passworddto.value)
        
        self.session.query(PasswordDto).add(passworddto)
        self.session.commit()