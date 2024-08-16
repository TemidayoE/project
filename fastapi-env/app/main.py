from fastapi import FastAPI,Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine, get_db
from .routers import movies,users,authentication,ratings, comments
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

models.Base.metadata.create_all(bind=engine)




app.include_router(movies.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(ratings.router)
app.include_router(comments.router)

@app.get("/")
def homepage():
    return {"message": "King: Welcome to my API"}



    
