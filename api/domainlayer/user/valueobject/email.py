
from dataclasses import dataclass


@dataclass(frozen=True)
class Email():
    """メールアドレスの値を保持するクラス

    Returns:
        [type]: Email
    """    
    _val: str 
    
    def __init__(self, value: str) -> None:
        """値をセット

        Args:
            __value (str): メールアドレスの値
        """        
        object.__setattr__(self, "_val", value)
    
    @property
    def value(self):
        """変数を隠蔽するための関数

        Returns:
            [type]: メールアドレスの値を返す
        """        
        return self._val