from fastapi import UploadFile, File
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    dob: datetime
    gender: str
    email: EmailStr
    password: str
    profile_photo: Optional[UploadFile] = File(None)

class UserOut(BaseModel):
    id: int
    name: str
    dob: datetime
    gender: str
    email: EmailStr
    profile_photo: Optional[UploadFile] = File(None)

    class Config:
        orm_mode = True