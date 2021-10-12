DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
      'user': 'azuma',
      'password': 'Azuma516',
      'host': 'localhost',
      'db-name': 'api'
  })
