from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.utils.hash import hash_password,verify_password
from src.repository.user_repo import create_user,get_user_by_email
from src.utils.jwt import create_access_token,create_refresh_token
from src.utils.logger import logger
from src.repository.role_repo import get_role_by_name
from src.repository.user_role_repo import assign_role

def register_user(db:Session,salutation:str,first_name:str,last_name:str,degree:str,degree_certificate:str,passing_year,email:str,password:str):
    try:
        user = get_user_by_email(db, email)
        if user:
            raise HTTPException(400, "User already exists")
        hashed_password = hash_password(password)
        new_user = create_user(db,salutation,first_name,last_name,degree,degree_certificate,passing_year, email,hashed_password)
        
        candidate_role = get_role_by_name(db, "candidate")
        if candidate_role:
            assign_role(db, new_user.id, candidate_role.id)

        return new_user
    except Exception as e:
        logger.error(str(e))
        raise e



def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(404, "User not found")
    if not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid password")
    roles = []

    for role in user.roles:
        roles.append(role.name)
    
    access = create_access_token({"user_id": str(user.id),"roles": roles})
    refresh = create_refresh_token({"user_id": str(user.id),"roles": roles})
    logger.info("Login successful")
    name=user.first_name
    surname=user.last_name
    return{
        "name":name,
        "surname":surname,
        "user_id": str(user.id),
        "roles": roles,
        "access_token": access,
        "refresh_token": refresh
    }




