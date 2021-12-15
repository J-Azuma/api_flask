from flask_mail import Message
from api.mail import mail

class sendVerifyUserMailService(object):
      ## メール送信用関数
  def sendUserVerifyMail(aUserData :dict):
      msg = Message(subject='仮登録のお知らせ' , recipients=[aUserData['email']])
      msg.body = "仮登録が完了しました。 \n\n以下のURLからアカウントを有効化してください。"
      mail.send(msg)
        