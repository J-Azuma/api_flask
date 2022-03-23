from abc import ABCMeta, abstractmethod

from api.domainlayer.password.password import Password

class IpasswordRepository(metaclass=ABCMeta):
    """パスワードリポジトリのインターフェース

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """    
    @abstractmethod
    def find(self, password) -> None:
        """idで検索する抽象メソッド

        Args:
            password ([type]): [description]
        """        
        pass
    
    @abstractmethod
    def add(self, password: Password) -> None:
        """パスワード永続化処理のインターフェース

        Args:
            password (Password): パスワードインスタンス
        """
        pass