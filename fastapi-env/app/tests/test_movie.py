import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db
from app import models, schemas

# Define the test database URL (PostgreSQL)
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Blockbuster200$@localhost/fastapi'

# Create a test engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the test database
models.Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_listed_movies():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json == {}

    

def test_list_a_movie():
    response = client.post("/", json = {
    "title": "string",
    "description": "string",
    "movie_director": "string",
    "genre": "string",
    "is_published": None,
    "id": 0,
    "created_at": "2024-08-15T02:54:43.421Z",
    "user_id": 0
  } )
    assert response.status_code == 201
    assert response.json == [ {
    "title": "string",
    "description": "string",
    "movie_director": "string",
    "genre": "string",
    "is_published": None,
    "id": 0,
    "created_at": "2024-08-15T02:54:43.421Z",
    "user_id": 0
  }]