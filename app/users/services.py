from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from app.users.models import User
from app.users.schemas import UserCreate, UserUpdate


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
