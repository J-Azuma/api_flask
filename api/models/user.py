from sqlalchemy.orm import query
from api.database import db ,marshmallow

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    # Flask=JWTはidという文字列でないと動作しないため
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, default="")
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String , nullable=True)
    is_verified = db.Column(db.Boolean , nullable=False, default=False)

    def __init__(self, email=None, password=None):
        self.username = ""
        self.email = email
        self.password = password
        self.is_verified = False
  
    def __repr__(self):
        return f'<User {self.username!r}>'

  
    def getUserList():
        from api.repositories.userRepository import userRepository
        user_list: list = userRepository.getUsers()

        if user_list == None:
            return []
        else:
            return user_list
          
    def registUser(aUserData :dict):
        user = User(email=aUserData['email'] , password=aUserData['password'])
        from api.repositories.userRepository import userRepository
        userRepository.insertUser(user)
        return user
        
        
    def verifyUser(aId: int):
        # ユーザIDに合致するレコードのis_verifyカラムをTrueにupdateする
        db.session.query(User).filter(User.id == aId).update({"is_verified" : 1})
        db.session.commit()
        
class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id' , 'username', 'email', 'password' , 'is_verified')
        