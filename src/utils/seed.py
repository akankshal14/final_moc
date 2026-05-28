from sqlalchemy.orm import Session
from src.utils.logger import logger

from src.utils.seed_roles import seed_roles
from src.utils.seed_superadmin import seed_superadmin


def seed(db: Session):
    try:
        seed_roles(db)
        seed_superadmin(db)
        logger.info("All seeds completed")
    except Exception as e:
        logger.error(f"Seeding failed: {str(e)}")