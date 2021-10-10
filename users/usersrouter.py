from fastapi import APIRouter, status, Depends
from .schema import SignUpModel
from config.database import get_db
from sqlalchemy.orm import Session
from .usersservice import UsersService
from .models import User
from config.token import get_currentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def createUser(user: SignUpModel, db: Session = Depends(get_db)):
    return UsersService.create_user(user=user, db=db)


@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user
