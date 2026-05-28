from sqlalchemy.orm import Session
from src.model.role_model import Role


def get_role_by_name(db: Session, name: str):
    return db.query(Role).filter(Role.name == name).first()

def get_role_by_role_id(db:Session,role_id):
    return db.query(Role).filter(Role.id == role_id ).first()