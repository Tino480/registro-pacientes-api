from fastapi import status, Depends, APIRouter
from app.users.models import User
from app.users import schemas
from app.users import services
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserGet])
def read_users(
    db: Session = Depends(get_db),
):
    return services.get_users(db)


@router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.UserGet
)
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return services.get_user(db, user_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserGet)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),

):
    return services.create_user(db, user)


@router.put(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.UserGet
)
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    
):
    return services.update_user(db, user_id, user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,

)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return services.delete_user(db, user_id)
