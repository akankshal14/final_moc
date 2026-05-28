from sqlalchemy.orm import Session
from src.model.user_model import User


def create_admin(db: Session,salutation: str,first_name: str,last_name: str,email: str,password_hash: str):
    user = User(
        salutation=salutation,
        first_name=first_name,
        last_name=last_name,
        degree="None",
        degree_certificate=None,
        passing_year=None,
        email=email,
        password_hash=password_hash
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

    
   