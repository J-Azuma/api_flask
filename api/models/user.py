from api.database import db ,marshmallow


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)

    def __init__(self, username=None):
        self.username = username 
  
    def __repr__(self):
        return f'<User {self.username!r}>'

  
    def getUserList():
        user_list: list = db.session.query(User).all()

        if user_list == None:
            return []
        else:
            return user_list

class UserSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('uid' , 'username')
        