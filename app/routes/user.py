from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from datetime import datetime

from app.services.db import get_db
from app.models.user_model import User
from app.utils.hash import hash_password
from app.utils.supabase_upload import upload_image_to_supabase

router = APIRouter()

@router.post("/register")

def register_user(
    name: str = Form(...),
    dob: str = Form(...),
    gender: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    profile_photo: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code = 400, detail = "Email already registered")
    
    hashed_pw = hash_password(password)

    dob_dt = datetime.fromisoformat(dob) # "YYYY-MM-DD"

    new_user = User (
        name = name,
        dob = dob_dt,
        gender = gender,
        email = email,
        password_hash = hashed_pw,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if profile_photo:
        photo_url = upload_image_to_supabase(profile_photo, str(new_user.id))
        new_user.profile_photo = photo_url
        db.commit()

    return {
        "id": new_user.id,
        "name": new_user.name,
        "dob": new_user.dob.isoformat(),
        "gender": new_user.gender,
        "profile_photo": new_user.profile_photo
    }