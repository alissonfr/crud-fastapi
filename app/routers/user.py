from typing import List
from fastapi import APIRouter, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserResponse, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user