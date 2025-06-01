from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError , jwt 
from settings import settings

SERECT_KEY = settings.serect_key
ALGORTIHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 3600

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expiration":expire})
    return jwt.encode(to_encode,SERECT_KEY,algorithm=ALGORTIHM)


