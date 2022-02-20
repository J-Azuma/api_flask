
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.user.user import User


class ValidateUser():
    """User集約のサービス。 まずはUserクラス内にロジックを書くことを検討しよう
    """    
    def __init__(self, userrepository: IuserRepository) -> None:
        """初期化

        Args:
            userrepository (IuserRepository): Userリポジトリのインターフェース
        """        
        self.userrepository = userrepository
    
    
    def exists(self, user: User) -> bool:
        """メールアドレスの重複判定

        Args:
            user (User): Userインスタンス

        Returns:
            bool: userインスタンスの有無(重複有無)
        """        
        user = self.userrepository.find_by_email(user)
        return user is None