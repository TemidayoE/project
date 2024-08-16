from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from typing import Optional, List
from app import models,schemas,utils, oauth2,database
from sqlalchemy.orm import Session


router = APIRouter(
  prefix= "/comment",
  tags= ["Comments"]
)

@router.post("/{id}")
def create_comment(comment: schemas.CommentCreate, id: int = models.Movies.id, db: Session = Depends(database.get_db),current_user: int = Depends(oauth2.get_current_user)):
    
    if comment.parent_comment_id:
        parent_comment = db.query(models.Comments).filter(models.Comments.id == comment.parent_comment_id).first()
        if not parent_comment:
            raise HTTPException(status_code=404, detail="Parent comment not found")

    else:
        comment.parent_comment_id = None
        
    new_comment = models.Comments(user_id=current_user.id, movie_id= id, comment= comment.comment, parent_comment_id=comment.parent_comment_id)

    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

    

@router.get("/", response_model=List[schemas.CommentResponse])
def list_comments(db: Session = Depends(database.get_db)):
    comments = db.query(models.Comments).all() 
    return comments
