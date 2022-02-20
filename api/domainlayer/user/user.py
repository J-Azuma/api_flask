from sqlalchemy import false
from ulid import ULID

from api.domainlayer.user.valueobject.email import Email

class User():
    """Userクラス
    """    
    def __init__(self, email: Email, is_verified: bool = False, id: str = str(ULID())) -> None:
        """Userインスタンスを初期化。再構成を考慮して、新規生成時はidをデフォルトで設定する

        Args:
            email (Email): メールアドレス
            is_verified (bool, optional): 有効化フラグ Defaults to False.
            id (str, optional): id Defaults to str(ULID()).
        """        
        self.__email: Email = email
        self.__is_verified: bool = is_verified
        self.__id: str = id
    
    @property
    def id(self) -> str:
        """idを返す

        Returns:
            str: id
        """        
        return self.__id
    
    @property
    def email(self) -> str:
        """メールアドレスを返す

        Returns:
            str: メールアドレス
        """        
        return self.__email.value
    
    @property
    def is_verified(self) -> bool:
        """有効化状態を保持

        Returns:
            bool: 有効化状態
        """        
        return self.__is_verified
    
    def verify(self) -> None:
        """アカウントを有効化する
        """        
        if not self.is_verified:
            self.__is_verified = True
    
    
        
    
    