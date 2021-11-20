from api.models.user import User
# from api.set_jwt import jwt
from api.database import db
from werkzeug.security import check_password_hash

def authenticate(email :str, password :str):
  # flask_sqlalchemy.BaseQueryクラスのオブジェクトを取得している
  
    user = db.session.query(User).filter_by(email = email).one()
    if user and check_password_hash(user.password, password):
        return user

def identity(payload :object):
    print(payload)
    uid = payload['identity']
    return db.session.query(User.uid).filter_by(uid = uid)

