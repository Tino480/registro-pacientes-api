from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.users import schemas, services

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserGet])
def read_users(
    db: Session = Depends(get_db),
):
    return services.get_users(db)


@router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.UserGet
)
def read_user(user_id: int, db: Session = Depends(get_db)):
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
    user: schemas.UserUpdate,
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


@router.get(
    "/consultations/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ConsultationGet],
)
def read_consultations(
    db: Session = Depends(get_db),
):
    return services.get_consultations(db)


@router.get(
    "/consultations/{consultation_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ConsultationGet,
)
def read_consultation(consultation_id: int, db: Session = Depends(get_db)):
    return services.get_consultation(db, consultation_id)


@router.post(
    "/consultations/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ConsultationGet,
)
def create_consultation(
    consultation: schemas.ConsultationCreate,
    db: Session = Depends(get_db),
):
    return services.create_consultation(db, consultation)


@router.put(
    "/consultations/{consultation_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ConsultationGet,
)
def update_consultation(
    consultation_id: int,
    consultation: schemas.ConsultationUpdate,
    db: Session = Depends(get_db),
):
    return services.update_consultation(db, consultation_id, consultation)


@router.delete(
    "/consultations/{consultation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_consultation(
    consultation_id: int,
    db: Session = Depends(get_db),
):
    return services.delete_consultation(db, consultation_id)
