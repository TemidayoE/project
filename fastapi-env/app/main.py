from fastapi import FastAPI,Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from app import models,schemas,utils
from app.database import engine, get_db
from app.routers import movies,users,authentication,ratings, comments

app = FastAPI()


app.include_router(movies.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(ratings.router)
app.include_router(comments.router)

@app.get("/")
def homepage():
    return {"message": "King: Welcome to my API"}



    
