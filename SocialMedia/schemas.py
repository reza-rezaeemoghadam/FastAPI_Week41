from pydantic import BaseModel
from datetime import date
from typing import Optional

class WriterBase(BaseModel):
    name:str
    date_of_birth: Optional[date] = None
    password:str

class PostBase(BaseModel):
    post_id:int
    title:str
    text:str
    image:str 
    writer_id:int
    
    class Config:
        orm_mode = True
        
class PostCreate(PostBase):
    pass

class Post(PostBase):
    pass

class CommentBase(BaseModel):
    comment_id:int
    title:str
    text:str
    post_id:int
    class Config:
        orm_mode = True
        
class ViewerBase(BaseModel):
    viewer_id:int
    name:str
    password:str
    class Config:
        orm_mode = True