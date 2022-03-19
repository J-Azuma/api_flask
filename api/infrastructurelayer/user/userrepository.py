
from http.client import INTERNAL_SERVER_ERROR
from typing import Union
from flask_restful import abort
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
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
            self.session.add(userdto)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            abort(INTERNAL_SERVER_ERROR)
    
    def find_by_email(self, user: User) -> Union[User, None]:
        """emailカラムでレコードを検索

        Args:
            user (User): ユーザオブジェクト

        Returns:
            Union[User, None]: レコード(存在しない場合Noneを返す)
        """        
        userdto: UserDto = UserDto.from_entity(user)
        email: str = userdto.email
        
        try:
            record: UserDto = self.session.query(UserDto).filter(UserDto.email == email).one()
        except NoResultFound:
            return None
        except SQLAlchemyError:
            raise SQLAlchemyError("ユーザ登録に失敗しました")
        
        return record.to_entity()
    
    def find_by_id(self, id: str) -> Union[User, None]:
        
        try:
            userdto: UserDto = self.session.query(UserDto).filter(UserDto.id == id)
        except NoResultFound:
            return None
        except SQLAlchemyError:
            raise SQLAlchemyError("ユーザの取得に失敗しました")
        
        return userdto.to_entity()