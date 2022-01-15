from abc import ABCMeta, abstractmethod

from api.domainlayer.movie.Movie import Movie

class ImovieReposirtory(metaclass=ABCMeta):
    """movieオブジェクトを操作するrepositoryの抽象クラス

    Args:
        metaclass ([type], optional): [description]. Defaults to ABCMeta.
    """    
    
    @abstractmethod
    def findby_id(self, id: int):
        """idでmovieオブジェクトを検索

        Args:
            id (int): 映画のid
        """        
        pass
    
    @abstractmethod
    def findby_name(self, name: str):
        """タイトルで映画を検索

        Args:
            name (str): 検索ワード
        """        
        pass