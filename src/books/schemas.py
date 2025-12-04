import uuid
from pydantic import BaseModel, ConfigDict
from datetime import date,datetime

class Book(BaseModel):
    uid:uuid.UUID
    title:str
    author:str
    publisher:str
    published_date:date
    language:str
    page_count:int
    created_at:datetime
    update_at:datetime

class BookCreateInputs(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    language: str
    page_count: int

class BookUpdateModel(BaseModel):
    title:str
    author: str
    publisher:str
    language:str
    page_count:int
