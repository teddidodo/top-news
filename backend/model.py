from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text, DateTime
from database import Base
from sqlalchemy.orm import relationship

class News(Base):
    __tablename__ = "news"
    id  = Column(Integer(), primary_key=True)
    search_when = Column(DateTime)
    title = Column(Text())
    published = Column(DateTime)
    link = Column(Text())
    summary = Column(Text())
