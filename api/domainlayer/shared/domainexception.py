
from http.client import BAD_REQUEST
from typing import Final
from flask import jsonify

class DomainException(Exception):
    
    def __init__(self, message: str) -> None:
        self.message: Final[str] = message
        
        
        
class BadRequestDomainException(DomainException):
    __code: Final[int] =  BAD_REQUEST
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.code: Final[int] = self.__code
    
    def handle_domain_exception(self):
        exception_dict: Final[dict] = self.__dict__
        return jsonify(exception_dict), self.__code
        