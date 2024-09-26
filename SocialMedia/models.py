from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base

class Writers(Base):
    __tablename__ = "writers" 
    writer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False) 
    date_of_birth = Column(Date, nullable=True)
    password = Column(String, nullable=False)

class Viewers(Base):
    __tablename__ = "viewers" 
    viewer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False) 
    password = Column(String, nullable=False)
     
class Posts(Base):
    __tablename__ = "posts"     
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    image = Column(String, nullable=False)
    writer_id = Column(Integer, ForeignKey("writers.writer_id"))
    
    # writer = relationship("Writers", back_populates="post")

class Comments(Base):
    __tablename__ = "comments"     
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    
    # post = relationship("Posts", back_populates="comment")