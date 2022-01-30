from datetime import datetime
from ulid import ULID

from api.infrastructurelayer.recordrepository import RecordRepository
from ..record.valueobject.watchdate import watchDate
from api.domainlayer.record.Irecordrepository import IrecordRepository

class Record():
    def __init__(self, watch_date: watchDate, user_id:int, movie_id:int, record_repository: IrecordRepository) -> None:
        self.__record_id: str = str(ULID())
        self.__watch_date: watchDate = watch_date
        self.__user_id: int = user_id
        self.__movie_id: int = movie_id
        
        # recordrepositoryへの依存を注入
        self.record_repository: IrecordRepository = record_repository
    
    
    def save(self) -> None:
        """オブジェクトを保存
        """        
        self.record_repository.save(self)
        