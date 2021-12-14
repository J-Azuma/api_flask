from flask_mail import Message
from api.models.user import User
from api.mail import mail

def ProRegistUser(aUserData :dict):
    # モデルクラスを呼び出しユーザ登録
    user : User = User.registUser(aUserData)
    # ユーザ登録が完了すれば仮登録完了メールを送信
    sendUserVerifyMail(aUserData)
    return user

## メール送信用関数
def sendUserVerifyMail(aUserData :dict):
    msg = Message(subject='仮登録のお知らせ' , recipients=[aUserData['email']])
    msg.body = "仮登録が完了しました。 \n\n以下のURLからアカウントを有効化してください。"
    mail.send(msg)