from sqlalchemy.orm import Session
from src.model.role_model import Role
from src.utils.logger import logger


def seed_roles(db: Session):
    roles = ["candidate", "admin", "superadmin", "diplomate"]
    for role in roles:
        exists = db.query(Role).filter(Role.name == role).first()
        if not exists:
            db.add(Role(name=role))
    db.commit()
    logger.info("Roles seeded successfully")