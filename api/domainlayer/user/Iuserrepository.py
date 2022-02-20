
from abc import ABCMeta, abstractclassmethod, abstractmethod

from api.domainlayer.user.user import User

class IuserRepository(metalass=ABCMeta):
    
    @abstractmethod
    def add(self, user: User) -> None:
        pass 
    
    @abstractmethod
    def find_by_email(self, user: User) -> None:
        pass