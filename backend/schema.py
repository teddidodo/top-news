from pydantic import BaseModel
from datetime import datetime

class NewsSchema(BaseModel):
    title: str
    published: str
    link: str
    description: str
    author: list
    publisher: str
    country: list
    category: list
    language: str
    keywords: list

class QuerySchema(BaseModel):
    query: str

class UserNewsSave(NewsSchema):
    query: str

class UserSchema(BaseModel):
    email: str
    password: str

class UserLogin(UserSchema):
    pass

class UserUpdateInformation(UserSchema):
    pass
class UserRegister(UserSchema):
    pass
