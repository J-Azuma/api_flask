from abc import ABC, ABCMeta, abstractmethod

from api.domainlayer.movie.Movie import Movie

class ImovieRepository(ABC):
    """movieオブジェクトを操作するrepositoryの抽象クラス

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """    
    
    @abstractmethod
    def find_by_id(self, id: int) -> Movie:
        """idでmovieオブジェクトを検索

        Args:
            id (int): 映画のid
        """        
        pass
    
    @abstractmethod
    def findby_name(self, name: str) -> Movie:
        """タイトルで映画を検索

        Args:
            name (str): 検索ワード
        """        
        pass