from sqlalchemy.orm import Session
from src.model.user_model import User
from src.model.role_model import Role
from src.utils.hash import hash_password
from src.utils.logger import logger
from src.config.settings import settings
import uuid


def seed_superadmin(db: Session):
    role = db.query(Role).filter(Role.name == "superadmin").first()
    if not role:
        logger.error("Superadmin role missing. Seed roles first.")
        return

    existing = (db.query(User).join(User.roles).filter(Role.name == "superadmin").first())
    if existing:
        logger.info("Superadmin already exists")
        return
    
    user = User(
        id=uuid.uuid4(),
        salutation=settings.SUPERADMIN_SALUTATION,
        first_name=settings.SUPERADMIN_FIRST_NAME,
        last_name=settings.SUPERADMIN_LAST_NAME,
        degree=None,
        degree_certificate=None,
        passing_year=None,
        email=settings.SUPERADMIN_EMAIL,
        password_hash=hash_password(settings.SUPERADMIN_PASSWORD)
    )
    user.roles.append(role)
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info("Superadmin created successfully from settings")