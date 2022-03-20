from click import echo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"), echo=True)

session_maker = sessionmaker(autocommit=False,
                             autoflush=False,
                             bind=engine)

session = scoped_session(session_maker)

Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from api.infrastructurelayer.user.userdto import UserDto
    from api.infrastructurelayer.password.passworddto import PasswordDto
    Base.metadata.create_all(bind=engine)


