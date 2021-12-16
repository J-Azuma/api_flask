from typing import List
from api.database import db
from api.models.user  import User


class userRepository(object):
  
  def getUsers() -> List[User]:
      users :List[User] = db.session.query(User).all()
      return users
    
  def insertUser(user :User):
      db.session.add(user)
      db.session.commit()
      return user