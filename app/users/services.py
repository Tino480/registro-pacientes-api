from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from app.users.models import Consultation, User
from app.users.schemas import (
    ConsultationCreate,
    ConsultationUpdate,
    UserCreate,
    UserUpdate,
)


def get_user_dict(user: User) -> dict:
    user_dict = user.__dict__
    return user_dict


def get_users(db: Session) -> list:
    users = db.query(User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No users found"
        )
    return list(map(get_user_dict, users))


def get_user(db: Session, user_id: int) -> dict:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return get_user_dict(user)


def create_user(db: Session, user: UserCreate) -> dict:
    new_user = User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return get_user_dict(new_user)


def update_user(db: Session, user_id: int, user: UserUpdate) -> dict:
    db_user_query = db.query(User).filter(User.id == user_id)
    if not db_user_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db_user_query.update(user.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return get_user_dict(db_user_query.first())


def delete_user(db: Session, user_id: int) -> Response:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(db_user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_consultation_dict(consultation: Consultation) -> dict:
    consultation_dict = consultation.__dict__
    return consultation_dict


def get_consultations(db: Session) -> list[dict]:
    consultations = db.query(Consultation).all()
    if not consultations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No consultations found"
        )
    return list(map(get_consultation_dict, consultations))


def get_consultation(db: Session, consultation_id: int) -> dict:
    consultation = (
        db.query(Consultation).filter(Consultation.id == consultation_id).first()
    )
    if not consultation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found"
        )
    return get_consultation_dict(consultation)


def create_consultation(db: Session, consultation: ConsultationCreate) -> dict:
    new_consultation = Consultation(**consultation.dict())
    try:
        db.add(new_consultation)
        db.commit()
        db.refresh(new_consultation)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return get_consultation_dict(new_consultation)


def update_consultation(
    db: Session, consultation_id: int, consultation: ConsultationUpdate
) -> dict:
    db_consultation_query = db.query(Consultation).filter(
        Consultation.id == consultation_id
    )
    if not db_consultation_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found"
        )
    db_consultation_query.update(
        consultation.dict(exclude_unset=True), synchronize_session=False
    )
    db.commit()
    return get_consultation_dict(db_consultation_query.first())


def delete_consultation(db: Session, consultation_id: int) -> Response:
    db_consultation = (
        db.query(Consultation).filter(Consultation.id == consultation_id).first()
    )
    if not db_consultation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Consultation not found"
        )
    db.delete(db_consultation)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
