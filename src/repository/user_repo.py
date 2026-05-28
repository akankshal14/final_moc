from sqlalchemy.orm import Session
from src.model.user_model import User
from sqlalchemy import func

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(func.lower(User.email)==func.lower(email)).first()


def create_user(db:Session,salutation:str,first_name:str,last_name:str,degree:str,degree_certificate:str,passing_year:int,email:str,password_hash:str):
    first_name = first_name.title()
    last_name = last_name.title()
    user=User(salutation=salutation,first_name=first_name,last_name=last_name,degree=degree,degree_certificate=degree_certificate,passing_year=passing_year,email=email,password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()




