from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://trxntssn:zJWzfMOJRShol9kXxiLAqldh0ZSzZ97N@hattie.db.elephantsql.com/trxntssn')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()