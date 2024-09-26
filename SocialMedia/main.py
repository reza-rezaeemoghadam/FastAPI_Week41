from schemas import CommentBase, PostBase, WriterBase, ViewerBase
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, create_tables
from crud import show_posts

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/api/v1/posts/", response_model=list[PostBase])
def post_list(db:Session=Depends(get_db)):
        data = show_posts(db)
        return data