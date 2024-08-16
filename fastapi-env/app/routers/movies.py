from fastapi import FastAPI,Response, status, HTTPException, Depends, APIRouter
from typing import Optional, List
from app import models,schemas,utils, oauth2
from app.database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
  prefix= "/movies",
  tags= ["Movies"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Movie)
def list_a_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    new_movie = models.Movies(**movie.dict(), user_id=current_user.id)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


@router.get("/", response_model= List[schemas.Movie])
def listed_movies(db: Session = Depends(get_db)):

    movies = db.query(models.Movies).all()
    return movies


@router.get("/{id}", response_model= schemas.Movie )
def listedMovie_by_ID(id:int ,db: Session = Depends(get_db)):
    movie = db.query(models.Movies).filter(models.Movies.id == id).first()
    if not movie:
         raise HTTPException(status.HTTP_404_NOT_FOUND,
                             detail= f'movie with id: {id}, not found, try another' )
    return movie


@router.put("/{id}",response_model= schemas.Movie)
def update_listedMovie(id: int, movie: schemas.Movie, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    movie_query = db.query(models.Movies).filter(models.Movies.id == id)
    existing_movie = movie_query.first()

    if existing_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with id: {id}, does not exist"
        )
    if movie.user_id != current_user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Not authorised to perform action" )
        
    movie_query.update(movie.dict(), synchronize_session=False)
    db.commit()
    
    return  movie_query.first()



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_a_movie(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    movie_query = db.query(models.Movies).filter(models.Movies.id == id)

    movie = movie_query.first()
    
    if movie == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'movie with id: {id}, does not exist')
    
    if movie.user_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= "Not authorised to perform action" )
    movie_query.delete(synchronize_session = False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)