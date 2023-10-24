from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from sqlalchemy.orm import relationship

class News(Base):
    __tablename__ = "News"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=True, server_default='uuid_generate_v4()')
    search_when = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    title = Column(Text())
    published = Column(Text())
    link = Column(Text())
    description = Column(Text())
    author = Column(ARRAY(Text()))
    publisher = Column(Text())
    country = Column(ARRAY(Text()))
    category = Column(ARRAY(Text()))
    keywords = Column(ARRAY(Text()))
    language = Column(Text())

    user_id = Column(UUID(as_uuid=True), ForeignKey('Users.id', ondelete='CASCADE'), server_default='uuid_generate_V4()')

    news_info = relationship('UserNews', back_populates='news')

class User(Base):
    __tablename__ = 'Users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=True, server_default='uuid_generate_v4()')
    email = Column(Text())
    password = Column(Text())

    user_info = relationship('UserNews', back_populates='user')

class Query(Base):
    __tablename__='Queries'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=True, server_default='uuid_generate_v4()')
    query = Column(Text())
    user_id = Column(UUID(as_uuid=True), ForeignKey('Users.id', ondelete='CASCADE'), server_default='uuid_generate_V4()')

    query_info = relationship('UserNews', back_populates='query')

class UserNews(Base):
    __tablename__='UserNews'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=True, server_default='uuid_generate_V4()')
    user_id = Column(UUID(as_uuid=True), ForeignKey('Users.id', ondelete='CASCADE'), server_default='uuid_generate_V4()')
    news_id = Column(UUID(as_uuid=True), ForeignKey('News.id', ondelete='CASCADE'), server_default='uuid_generate_V4()')
    query_id = Column(UUID(as_uuid=True), ForeignKey('Queries.id', ondelete='Set NULL'), server_default='uuid_generate_V4()')

    user = relationship('User', back_populates='user_info')
    news = relationship('News', back_populates='news_info')
    query = relationship('Query', back_populates='query_info')
