from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from typing import Optional, List
from app import models,schemas,utils, oauth2,database
from sqlalchemy.orm import Session

router = APIRouter(
  tags= ["ratings"],
  prefix= "/ratings"
)

@router.post("/", status_code= status.HTTP_201_CREATED)
def rate_a_movie(rating: schemas.Ratings, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    movie = db.query(models.Movies).filter(models.Movies.id == rating.movie_id).first()
    if not movie:
      raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Movie with id : {rating.movie_id} does not exist')
    
    rating_query = db.query(models.Ratings).filter(models.Ratings.movie_id == rating.movie_id, models.Ratings.user_id == current_user.id)
    found_rating = rating_query.first()
    
    if found_rating:
      raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= f"You already rated movie with id: {rating.movie_id}")
   
    
    new_rating = models.Ratings(movie_id = rating.movie_id, user_id = current_user.id, movie_rating = rating.rating)
    db.add(new_rating)
    db.commit()
    
    return { "message": "You have successfully rated this movie"}
          
    

@router.get("/", response_model= List[schemas.RatingsResponse])
def movie_ratings(db: Session = Depends(database.get_db)):
  
  ratings = db.query(models.Ratings).all()
  return ratings
