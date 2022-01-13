from dataclasses import dataclass
from datetime import date, datetime

@dataclass(frozen=True)
class watchDate():
    
    value: date
    
    def __init__(self, value: date) -> None:
        
        if not isinstance(value, date):
            raise TypeError("日付を入力してください")
        
        if self.is_future_date(value):
            raise ValueError("明日以降の日時は選択できません。")
        
        
        object.__setattr__(self, "value" , value)
    
    
    @classmethod
    def is_future_date(cls, value: date) -> bool:
        today  = date.today()
        return today < value