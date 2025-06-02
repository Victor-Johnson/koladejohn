from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
#import schemas
from schemas.schemas import Blogpost
import models
from utils.rbacdepend import get_current_user, require_admin

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/", response_model=Blogpost)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db), _: models.User = Depends(require_admin)):
    new_blog = models.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/", response_model=list[schemas.Blogpost])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

@router.put("/{blog_id}", response_model=schemas.Blogpost)
def update_blog(blog_id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db), _: models.User = Depends(require_admin)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    for key, value in blog.dict().items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog

@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db), _: models.User = Depends(require_admin)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Deleted"}
