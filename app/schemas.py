 
from pydantic import BaseModel, conint
from datetime import datetime
from pydantic import EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    username: Optional[str] = "Unnamed"

class UserResponse(BaseModel):
    id: int
    username: str
    phone_number: Optional[str] = None

class UserUpdate(BaseModel):
    phone_number: Optional[str] = None
    username: Optional[str] = "Unnamed"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    # created_at: datetime
    user_id: int
    user: UserResponse

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]



class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1) # type: ignore
