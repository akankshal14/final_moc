from sqlalchemy.orm import Session
from src.model.user_role_model import user_roles


def get_role_by_user_id(db: Session, id):
    return db.query(user_roles).filter(user_roles.user_id == id).first()

def assign_role(db, user_id, role_id):
    db.execute(
        user_roles.insert().values(
            user_id=user_id,
            role_id=role_id
        )
    )

    db.commit()