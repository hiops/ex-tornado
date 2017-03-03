# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from datetime import datetime
import hashlib

from settings import DB_CONFIG, PASSWD_SALT

engine = create_engine(DB_CONFIG, pool_recycle=5, poolclass=NullPool)

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
    password_hash = Column('password', String(50), nullable=False)
    created_on = Column('created_on', DateTime(), default=datetime.now)
    updated_on = Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        return self.password_hash
    @password.setter
    def password(self,passwd):
        self.password_hash =  self.gen_password_hash(passwd)

    def gen_password_hash(self,passwd):
        return hashlib.sha1("%s|%s|%s" % (passwd,self.username,PASSWD_SALT)).hexdigest()
    def check_password_hash(self,passwd):
        if self.password_hash == self.gen_password_hash(passwd):
            return True
        else:
            return False

def init_data():
    db = DB_Session()
    user = User(
        user_id=9,
        username='9@ops.com',
        email_address = '9@ops.com',
        phone = 12345678901,
        password = 'www.ops.com'
    )
    ins = db.add(user)
    print ins
    db.commit()
def test_data():
    db = DB_Session()
    user = db.query(User).filter(User.user_id==9).first()
    print user.__dict__
    print user.username
    print "check password:"
    password_raw = "ww.ops.com"
    print user.check_password_hash(password_raw)
    print user.gen_password_hash(password_raw)
    print user.password_hash

if __name__ == '__main__':
    #init_db()
    #drop_db()
    #init_data()
    test_data()
