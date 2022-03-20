from typing import Union
from sqlalchemy import Column, String, Boolean
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email
from api.infrastructurelayer.database import Base


class UserDto(Base):
    """UserエンティティをDBとやりとりする前に詰め替えるDTO

    Args:
        db (_type_): _description_
    """    
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Flask=JWTはidという文字列でないと動作しないため
    id = Column(String, primary_key=True, unique=True)
    email  = Column(String, nullable=False, unique=True)
    is_verified = Column(Boolean , nullable=False, default=False)
    
    
    def to_entity(self) -> User:
        """DTOからエンティティを作成

        Returns:
            User: Userクラスインスタンス
        """        
        return User(
            self.id,
            Email(self.email),
            self.is_verified
        )
        
    @staticmethod
    def from_entity(user: User) -> 'UserDto':
        """エンティティからDTOを作成

        Args:
            user (User): Userクラスインスタンス

        Returns:
            UserDto: DTO
        """        
        return UserDto(
            id = user.id,
            email = user.email,
            is_verified = user.is_verified
        )