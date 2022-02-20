from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from password.password import Password

class ValidatePassword():
    """パスワードの重複確認
    """    
    def __init__(self, passwordrepository: IpasswordRepository):
        """インスタンスの初期化
            リポジトリのインターフェースをDI
        Args:
            passwordrepository (IpasswordRepository): リポジトリのインターフェース
        """        
        self.passwordrepository = passwordrepository
    
    def exists(self, password: Password) -> bool:
        """パスワードの重複確認

        Args:
            password (Password): Passwordクラスのインスタンス

        Returns:
            [type]: 重複有無を真偽値で返す
        """        
        password = self.passwordrepository.find(password)
        return password is None