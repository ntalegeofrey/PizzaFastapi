from fastapi import Depends
from config.database import get_db
from .models import User
from .schema import SignUpModel
from sqlalchemy.orm import Session
from config.Hashing import Hashing


class UsersService:
    def get_user(email: str, db: Session = Depends(get_db)):
        return db.query(User).filter(User.email == email).first()

    def create_user(user: SignUpModel, db: Session = Depends(get_db)):

        db_user = User(
            username=user.username,
            email=user.email,
            password=Hashing.bcrypt(user.password),
            is_staff=user.is_staff,
            is_active=user.is_active,
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user
