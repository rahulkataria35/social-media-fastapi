from fastapi import Body, Depends, FastAPI, Response,status, HTTPException, APIRouter

from database import get_db
import schemas
import utils
import models

from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=['Users'])

# create user

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def user(user:schemas.User, db: Session=Depends(get_db)): 
    # hash the password
    hashed_pswd =utils.hash(user.password)
    user.password = hashed_pswd

    new_user = models.User(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model= schemas.UserOut)
def get_user(id: int, db: Session= Depends(get_db)):
    user_data = db.query(models.User).filter(models.User.id==id).first()

    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with id: {id} does not exist")

    return user_data