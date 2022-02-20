
from typing import Union

from mysqlx import DatabaseError
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.user.user import User
from api.infrastructurelayer.user.userdto import UserDto
from api.database import db

class UserRepository(IuserRepository):
    
    def __init__(self) -> None:
        self.session = db.session
    
    def add(self, user: User) -> None:
        """ ユーザを追加

        Args:
            user (User): ユーザインスタンス

        Raises:
            e: データベースエラー
        """        
        userdto: UserDto = UserDto.from_entity(user)
        try:
            self.session.query(UserDto).add(userdto)
            self.session.commit()
        except DatabaseError as e:
            raise e
    
    def find_by_email(self, user: User) -> Union[User, None]:
        pass