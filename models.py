# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import Column
from sqlalchemy.types import Integer

from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime

from settings import db_config

#engine = create_engine(db_config, pool_recycle=5, poolclass=NullPool)
engine = create_engine(db_config, pool_recycle=5, poolclass=NullPool)

DB_Session = sessionmaker(bind=engine)
BaseModel = declarative_base()


def init_db():
    BaseModel.metadata.create_all(engine)


def drop_db():
    BaseModel.metadata.drop_all(engine)


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column('user_id', Integer(), primary_key=True)
    username = Column('username', String(15), nullable=False, unique=True)
    email_address = Column('email_address', String(255), nullable=False)
    phone = Column('phone', String(20), nullable=False)
    password = Column('password', String(25), nullable=False)
    created_on = Column('created_on', DateTime(), default=datetime.now)
    updated_on = Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

def init_data():
    db = DB_Session()
    user = User(
        user_id=12345,
        username='hello1@ops.com',
        email_address = 'hello1@ops.com',
        phone = 12345678901,
        password = 'www.ops.com'
    )
    ins = db.add(user)
    print ins
    db.commit()
def test_data():
    db = DB_Session()
    user = db.query(User).filter(User.user_id==12345).all()
    print user[0].__dict__
    print user[0].username

if __name__ == '__main__':
    #init_db()
    #init_data()
    test_data()
