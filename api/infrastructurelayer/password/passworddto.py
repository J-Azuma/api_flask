from ast import Pass
from tkinter import CASCADE
from typing import Union
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint
from api.database import db
from api.domainlayer.password.password import Password

class PasswordDto(db.Model):
    
    __tablename__ = 'passwords'
    __table__args__ = {'extend_existing': True}
    
    user_id = db.Column(db.String, ForeignKey('user.id' , ondelete=CASCADE), primary_key=True, unique=True)
    value  = db.Column(db.String, primary_key=True, unique=True)
    
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