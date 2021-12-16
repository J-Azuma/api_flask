from api.database import db
from api.models.user  import User


class userRepository(object):

  def insertUser(user :User):
      db.session.add(user)
      db.session.commit()
      return user