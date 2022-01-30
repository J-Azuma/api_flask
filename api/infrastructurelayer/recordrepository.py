from ..domainlayer.record.Irecordrepository import IrecordRepository
from ..domainlayer.record.record import Record

class RecordRepository(IrecordRepository):
    
    def save(self, record: Record) -> None:
        """recordクラスオブジェクトを永続化

        Args:
            record (Record): recordオブジェクト
        """        
        pass