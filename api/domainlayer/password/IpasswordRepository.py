from abc import ABCMeta, abstractmethod

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
    def add(self, password) -> None:
        pass