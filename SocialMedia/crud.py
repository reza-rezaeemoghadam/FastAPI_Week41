from models import Viewers, Writers, Posts, Comments
from sqlalchemy.orm import Session

#TODO:Use async 
def show_posts(db:Session):
        data = db.query(Posts).all()
        return data

