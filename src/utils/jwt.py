import jwt
from datetime import datetime, timedelta, timezone
from src.config.settings import settings

SECRET_KEY=settings.SECRET_KEY
ALGORITHM=settings.ALGORITHM
MINUITES=settings.ACCESS_TOKEN_EXPIRE_MINUITES
DAYS=settings.REFRESH_TOKEN_EXPIRE_DAYS

def create_access_token(data:dict):
    payload=data.copy()
    payload["type"]="access"
    payload["exp"]=datetime.now(timezone.utc)+timedelta(minutes=MINUITES)
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def create_refresh_token(data:dict):
    payload=data.copy()
    payload["type"]="refresh"
    payload["exp"]=datetime.now(timezone.utc)+timedelta(days=DAYS)
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

