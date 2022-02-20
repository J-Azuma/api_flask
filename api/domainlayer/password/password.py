
from typing import Final
from click import BadParameter

from flask_restful import abort

from api.presentationlayer.shared.exception.exceptionhandler import BadRequestException


class Password():
    """ユーザの認証情報を保持する
    """    
    def __init__(self, id: str, value: str):
        """Passwordオブジェクトを初期化

        Args:
            id (str): ユーザid
            value (str): パスワード文字列
        """        
        USER_ID_LENGTH: Final[int] = 26
        
        if len(id) != USER_ID_LENGTH:
            raise BadRequestException("ユーザIDの値が不正です。")
        
        self.__user_id: str = id
        self.__value: str = value
        
    
    @property
    def user_id(self) -> str:
        """idを返す

        Returns:
            str: インスタンスのid
        """        
        return self.__user_id
    
    @property
    def value(self) -> str:
        """パスワードの値を返す

        Returns:
            str: パスワード
        """        
        return self.__value
    
    def change(self, value: str):
        """パスワードの値を変更する

        Args:
            value (str): 変更後の値
        """        
        self.__value = value