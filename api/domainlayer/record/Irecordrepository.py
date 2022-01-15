from abc import ABCMeta, abstractmethod

class IrecordRepository(metaclass=ABCMeta):
    """recordオブジェクトを保存するリポジトリのインターフェース

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """    
    
    @abstractmethod        
    def save(self, record) -> None:
        """保存処理の抽象メソッド

        Args:
            record (Record): 循環参照回避のために型を省略
        """        
        pass 
    