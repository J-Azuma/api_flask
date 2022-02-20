
from http.client import BAD_REQUEST
from flask_restful import abort

from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.domainlayer.password.service.validatepassword import ValidatePassword
from api.domainlayer.password.password import Password
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.user.service.validateuser import ValidateUser
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email

class CreateUser():
    """ユーザ作成ユースケース
    """    
    def __init__(self, userrepository: IuserRepository, passwordrepository: IpasswordRepository, validateuser: ValidateUser, valudatepassword: ValidatePassword):
        """インスタンス初期化

        Args:
            userrepository (IuserRepository): 
            passwordrepository (IpasswordRepository): [description]
            userservice (UserService): [description]
            passwordservice (PasswordService): [description]
        """        
        self.userrepository = userrepository
        self.passwordrepository = passwordrepository
        self.userservice: ValidateUser = validateuser
        self.passwordservice: ValidatePassword = valudatepassword
    
    def register(self, param: dict) -> None:
        """ユーザ作成処理

        Args:
            param (dict): ユーザの入力値(バリデーションはプレゼンテーション層)
        """        
        # ユーザ作成
        email: Email = Email(param["email"])
        user: User = User(email)
        password: Password = Password(user.id, param["password"])
        
        if self.__duplicate(user,password):
            abort(BAD_REQUEST, description={"message" : "メールアドレスまたはパスワードが不正な値です。"})
        
        # トランザクション処理にします
        self.userrepository.add(user)
        self.passwordrepository.add(password)
    
    def __duplicate(self, user: User, password: Password) -> bool:
        """メールアドレスかパスワードの重複を判定

        Args:
            user (User): Userオブジェクト
            password (Password): Passwordオブジェクト

        Returns:
            bool: 重複有無
        """        
        return self.__duplicate_email(user) or self.__duplicate_password(password)
    
    def __duplicate_email(self, user: User) -> bool:
        """メールアドレス重複判定をラッピング

        Args:
            user (User): Userクラスのインスタンス

        Returns:
            bool: 重複有無
        """        
        return self.userservice.exists(user)
    
    def __duplicate_password(self, password: Password) -> bool:
        """パスワード重複判定ロジックをラッピング

        Args:
            password (Password): Passwordインスタンス

        Returns:
            bool: 重複有無
        """        
        return self.passwordservice.exists(password)
        

        