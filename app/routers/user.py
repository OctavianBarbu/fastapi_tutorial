from .. import schemas, models, utils, oath2
from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model= List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db), current_user: int = 
                 Depends(oath2.get_current_user)):
    users = db.query(models.User).all()
    return users

@router.put("/", response_model=schemas.UserResponse)
def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db), current_user: int = 
                 Depends(oath2.get_current_user)):
    user_query = db.query(models.User).filter(models.User.id == current_user.id)
    user_to_update = user_query.first()
    user_to_update.phone_number = user.phone_number
    user_to_update.username = user.username
    db.commit()
    db.refresh(user_to_update)

    return user_to_update


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db), current_user: int = 
                 Depends(oath2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user with id: {id} does not exist.")
    
    return user
