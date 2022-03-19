
from injector import Injector

from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.movie.Imovierepository import ImovieRepository
from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.domainlayer.user.service.validateuser import ValidateUser
from api.infrastructurelayer.user.userrepository import UserRepository
from api.infrastructurelayer.movie.movierepository import MovieRepository
from api.infrastructurelayer.password.passwordrepository import PasswordRepository

class Dependency():
    """DIコンテナ用クラス
    """    
    def __init__(self) -> None:
        """Injectorクラスオブジェクトを戻す
        """        
        self.injector = Injector(self.__class__.config)
        
    
    @staticmethod
    def config(binder):
        """依存関係解決用メソッド

        Args:
            binder (_type_): binder
        """        
        binder.bind(IuserRepository, UserRepository)
        binder.bind(ImovieRepository, MovieRepository)
        binder.bind(IpasswordRepository, PasswordRepository)
        binder.bind(ValidateUser, ValidateUser)
    
    def resolve(self, cls):
        """依存関係を解決し、引数で渡したクラスのインスタンスを返却

        Returns:
            _type_: 引数クラスのインスタンス
        """        
        return self.injector.get(cls)