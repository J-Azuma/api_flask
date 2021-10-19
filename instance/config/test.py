DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'Azuma516',
      'host': 'localhost',
      'db-name': 'api_unit'
  })
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
TESTING = True