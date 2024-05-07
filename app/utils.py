from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash(string):
    return pwd_context.hash(string)

def verify(plain_pswd, hashed_pswd):
    return pwd_context.verify(plain_pswd, hashed_pswd)