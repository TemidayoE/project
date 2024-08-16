from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime,Float
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    movie_director = Column(String,nullable=False)
    genre = Column(String,nullable=False)
    is_published = Column(Boolean,server_default="True")
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable = False) 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable= False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class Ratings(Base):
     __tablename__ = "ratings"
     
     user_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable = False, primary_key= True) 
     movie_id = Column(Integer, ForeignKey("movies.id", ondelete= "CASCADE"), nullable = False, primary_key= True)
     movie_rating = Column(Float, nullable=False )


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    comment = Column(String, nullable=False)
    parent_comment_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    

