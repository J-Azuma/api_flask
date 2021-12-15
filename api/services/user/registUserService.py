from flask_mail import Message
from api.models.user import User
from api.mail import mail

class registUserService(object):
        
  def ProRegistUser(aUserData :dict):
      # モデルクラスを呼び出しユーザ登録
      user : User = User.registUser(aUserData)
      return user

