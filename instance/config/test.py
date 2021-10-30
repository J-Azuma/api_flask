DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'azuma',
      'password': 'Azuma_516',
      'host': 'localhost',
      'db_name': 'api_unit'
  })
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
TESTING = True