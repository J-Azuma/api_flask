from tokenize import String
from typing import Union
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, String
from api.database import db
from api.domainlayer.password.password import Password
from api.infrastructurelayer.database import Base

class PasswordDto(Base):
    
    __tablename__ = 'passwords'
    __table__args__ = {'extend_existing': True}
    
    user_id = Column(String, ForeignKey('users.id' , ondelete="CASCADE"), primary_key=True, unique=True)
    value  = Column(String, primary_key=True, unique=True)
    
    def to_entity(self) -> Password:
        
        return Password(
            self.user_id,
            self.value
        )
    
    
    @staticmethod
    def from_entity(password: Password) -> 'PasswordDto':
        return PasswordDto(
            user_id = password.user_id,
            value = password.value
        )