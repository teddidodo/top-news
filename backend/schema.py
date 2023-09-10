from pydantic import BaseModel

class NewsSchema(BaseModel):
    search_when: str
    title: str
    published: str
    link: str
    summary: str