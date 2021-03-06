from typing import Union
from injector import inject
from api.domainlayer.shared.domainexception import BadRequestDomainException
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.user.user import User


class ValidateUser():
    """User集約のサービス。 まずはUserクラス内にロジックを書くことを検討しよう
    """    
    @inject
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
        userrecord: Union[User, None] = self.userrepository.find_by_email(user)
        return userrecord is not None
    
    def validate(self, user: User):
        """メールアドレス重複時に例外送出

        Args:
            user (User): ユーザエンティティ

        Raises:
            BadRequestDomainException: 入力値を原因とする例外
        """
        if self.exists(user):
            raise BadRequestDomainException("メールアドレスが重複しています")