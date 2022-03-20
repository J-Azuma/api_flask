from ctypes import Union
from http.client import INTERNAL_SERVER_ERROR
from flask_restful import abort
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError

from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.infrastructurelayer.database import session
from api.domainlayer.password.password import Password
from api.infrastructurelayer.password.passworddto import PasswordDto

class PasswordRepository(IpasswordRepository):
    
    def __init__(self) -> None:
        self.session = session
        
    def add(self, password: Password) -> None:
        """レコードを追加

        Args:
            password (_type_): パスワードインスタンス
        """        
        passworddto: PasswordDto = PasswordDto.from_entity(password)
        passworddto.value = generate_password_hash(passworddto.value)
        
        try:
            self.session.add(passworddto)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            abort(INTERNAL_SERVER_ERROR)
    
    def find(self, password) -> None:
        pass