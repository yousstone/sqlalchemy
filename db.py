# coding=utf8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('mysql+mysqldb://root@localhost:3306/blog')
Base = declarative_base()
Base.metadata.create_all(engine)

def UserInfo(Base):

	__table__ = 'userinfos'

	id = Column(Integer, primary_key=True)
	name = Column(String(64))i
	qq = Column(String(11))
	phone = Column(String(11))
	link = Column(String(64))
	user_id = Column(Integer, ForeignKey('users.id'))

class User(Base):

	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	username = Column(String(64), nullable=False, index=True)


	password = Column(String(64), nullable=False)
	email = Column(String(64), nullable=False, index=True)
	articles = relationship('Article', backref='author')
	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__,self.username)
	
	

class Article(Base):
	
	__table__ = 'articles'

	id = Column(Integer, primary_kye=True)
	title = Column(String(255), nullable=False,index=True)
	content = Column(text)
	user_id = Column(Integer, ForeignKey('uers.id'))

	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__,self.username)
