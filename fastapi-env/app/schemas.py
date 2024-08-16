from pydantic import BaseModel, EmailStr, confloat, ConfigDict
from datetime import datetime
from typing import Optional

class MovieBase(BaseModel):
    title: str
    description: str
    movie_director: str
    genre: str
    is_published: bool = True

class MovieCreate(MovieBase):
    pass

class Movie(MovieCreate):
    id: int
    created_at: datetime
    user_id: int

    class ConfigDict:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class ConfigDict:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Ratings(BaseModel):
    movie_id: int
    rating: confloat(gt=0.9, lt=10.1)

class RatingsResponse(Ratings):
    user_id: int

    class ConfigDict:
        from_attributes = True

class Comments(BaseModel):
    comment: str
    parent_comment_id: Optional[int] = None

class CommentCreate(Comments):
    pass

class CommentResponse(Comments):
    id: int
    user_id: int
    movie_id: int
    created_at: datetime
    
    class ConfigDict:
        from_attributes = True
