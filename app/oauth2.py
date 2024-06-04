from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas, models, database
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict) -> str:
    """
    Create an access token with the provided data
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str, credential_exception):
    """
    Verify an access token and return the corresponding token data.

    Args:
        token (str): The access token to verify.
        credential_exception: The exception to raise if the token is invalid.

    Returns:
        Optional[schemas.TokenData]: The token data if the token is valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise credential_exception
        return schemas.TokenData(id=str(user_id))
    
    except JWTError:
        raise credential_exception
    


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    """
    Retrieve the current user based on the provided token.

    Args:
        token (str): The access token provided by the client.
        db (Session): The database session.

    Returns:
        models.User: The current user.

    Raises:
        HTTPException: If the token is invalid or cannot be verified.
    """
    try:
        token_data = verify_access_token(token)
        user = db.query(models.User).filter(models.User.id == token_data.id).first()
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )