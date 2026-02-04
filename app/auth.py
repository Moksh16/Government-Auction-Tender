from app import models, schemas, script
from app import utils
from fastapi import Depends,APIRouter,status,HTTPException,Response, Session
from app.db import get_db, sessionmaker,SessionLocal


router = APIRouter()


@router.post("/signin", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserSigin , db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password[:72])
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def login(user: schemas.UserLogin, db:Session= Depends(get_db)):
    check_user = db.query(user.Email_id).filter()