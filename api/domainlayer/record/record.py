from ulid import ULID
from ..record.valueobject.watchdate import watchDate

class Record():
    def __init__(self, watch_date: watchDate, user_id:int, movie_id:int) -> None:
        self.__record_id: str = str(ULID())
        self.__watch_date: watchDate = watch_date
        self.__user_id: int = user_id
        self.__movie_id: int = movie_id
    
    
        
        
        
        