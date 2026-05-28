from fastapi import Depends, HTTPException
from src.dependencies.auth_dependency import get_current_user

def require_role(*roles):
    def checker(current_user = Depends(get_current_user)):
        user_roles = current_user.get("roles", [])
        for role in roles:
            if role in user_roles:
                return current_user
        raise HTTPException(403,"Access Denied")
    return checker