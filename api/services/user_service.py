from api.models.user import User
from api.mail import mail

def ProRegistUser(aUserData :dict):
    # モデルクラスを呼び出しユーザ登録
    User.registUser(aUserData)
    # ユーザ登録が完了すれば仮登録完了メールを送信
    

## メールオブジェクト作成用関数
#def BuildMail():
  
## メール送信用関数
#def sendUserVerifyMail():