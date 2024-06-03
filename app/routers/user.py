from fastapi import Body, Depends, FastAPI, Response,status, HTTPException, APIRouter

from database import get_db
import schemas
import utils
import models

from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=['Users'])

# create user

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    # Hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="User already exists")
    
    # new_user = models.User(**user.model_dump())

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)) -> schemas.UserOut:
    """
    Get a user by ID.

    Args:
        id (int): The ID of the user to retrieve.
        db (Session): The database session.

    Raises:
        HTTPException: 404 if the user does not exist.

    Returns:
        schemas.UserOut: The retrieved user data.
    """
    user_data = db.query(models.User).filter(models.User.id == id).first_or_404()

    return user_data