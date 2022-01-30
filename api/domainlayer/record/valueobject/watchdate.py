from dataclasses import dataclass
from datetime import date, datetime

@dataclass(frozen=True)
class watchDate():
    
    value: datetime
    
    def __init__(self, value: datetime) -> None:
        
        if not isinstance(value, datetime):
            raise TypeError("日付を入力してください")
        
        if self.is_future_date(value):
            raise ValueError("明日以降の日時は選択できません。")
        
        
        object.__setattr__(self, "value" , value)
    
    
    @classmethod
    def is_future_date(cls, value: datetime) -> bool:
        today  = datetime.today()
        return today < value