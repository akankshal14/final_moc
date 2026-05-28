from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.utils.jwt import decode_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = decode_token(token)
        if payload.get("type") != "access":
            raise HTTPException(401, "Invalid token type")
        return payload
    except Exception:
        raise HTTPException(401, "Invalid or expired token")