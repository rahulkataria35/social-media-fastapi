from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional, Union
from pydantic.types import conint

class User(BaseModel):
    email: EmailStr
    password: str
    phone_number: Optional[Union[str, None]] = None  # Allow both string and None

    @validator("phone_number")
    def validate_phone_number(cls, v: Optional[Union[str, None]]):
        if v is not None:
            # Ensure it's a string
            if not isinstance(v, str):
                raise ValueError("phone_number must be a string")

            # Check length and format
            if not (10 <= len(v) <= 12):
                raise ValueError("phone_number must be between 10 and 12 characters")

            # Only perform numerical checks if it's actually numerical
            if v.isdigit():
                return v
                

class UserOut(BaseModel):
    email: str
    id: int

    class Config:
        orm_mode = True  # replace from_attributes with orm_mode


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# create schemas for the request body
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


# create a schema for Response
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


class PostData(PostBase):
    Post: Post
    vote: int

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1) # type: ignore
