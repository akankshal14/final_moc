from sqlalchemy.orm import Session
from src.model.enrollment_model import Enrollment
from uuid import UUID

def create_enrollment(db: Session, slot_id, candidate_id):
    enrollment = Enrollment(slot_id=slot_id,candidate_id=candidate_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment


def get_enrollment_by_user(db: Session, candidate_id):
    return db.query(Enrollment).filter(Enrollment.candidate_id == candidate_id).first()

def update_enrollment(db: Session,enrollment: Enrollment):
    db.commit()
    db.refresh(enrollment)
    return enrollment

def get_enrollment_by_id(db: Session,enrollment_id: UUID):
    return (db.query(Enrollment).filter(Enrollment.id == enrollment_id).first())