from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'Azuma_516',
      'host': 'localhost',
      'db_name': 'api'
  }))

session_maker = sessionmaker(autocommit=False,
                             autoflush=False,
                             bind=engine)

session = scoped_session(session_maker)

Base = declarative_base()
Base.query = session.query_property()

