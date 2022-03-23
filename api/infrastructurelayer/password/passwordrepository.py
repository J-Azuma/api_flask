from http.client import INTERNAL_SERVER_ERROR
from flask_restful import abort
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError

from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.domainlayer.password.password import Password
from api.infrastructurelayer.password.passworddto import PasswordDto
from api.infrastructurelayer.database import session
class PasswordRepository(IpasswordRepository):
    
    def __init__(self) ->None:
        self.session = session
    
    def add(self, password: Password) -> None:
        """レコードを追加

        Args:
            password (_type_): パスワードインスタンス
        """        
        passworddto: PasswordDto = PasswordDto.from_entity(password)
        passworddto.value = generate_password_hash(passworddto.value)
        
        self.session.add(passworddto)
        
    def find(self, id: str) -> Password:
        try:
            passworddto: PasswordDto = self.session.query(PasswordDto).filter(PasswordDto.user_id == id).one()
        except:
            raise SQLAlchemyError("aaa")
        
        return passworddto.to_entity()