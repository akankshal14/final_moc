from sqlalchemy.orm import Session
from uuid import UUID
from src.repository.enrollment_repo import get_enrollment_by_user,create_enrollment,update_enrollment,get_enrollment_by_id
from fastapi import HTTPException
from src.utils.logger import logger
from src.repository.user_repo import get_user_by_id
from datetime import datetime

def enroll_user(db:Session, slot_id:UUID, candidate_id:UUID):
    try:
        user=get_user_by_id(db,candidate_id)
        if not user:
            raise HTTPException(404,"user not found")
        
        user_role=[role.name.lower() for role in user.roles]
        if "candidate" not in user_role:
            raise HTTPException(400,"only the user with candidate role can enroll ")
        existing = get_enrollment_by_user(db, candidate_id)
        if existing:
            raise HTTPException(400, "candidate is already enrolled")

        enrollment = create_enrollment(db, slot_id, candidate_id)
        if not enrollment:
            raise HTTPException(404, "enrollment not found")
        logger.info("user enrolled sucessfully")
        return enrollment
    except Exception as e:
        logger.error(f"enroll user error:{str(e)}")
        raise e

def update_enrollment_status(db: Session,enrollment_id: UUID,is_payed: bool ,is_pass: bool ):
    enrollment = get_enrollment_by_id(db, enrollment_id)
    if not enrollment:
        raise HTTPException(404,"Enrollment not found")
    if is_payed is not None:
        if enrollment.is_payed:
            raise HTTPException(400,"Payment already completed")
        enrollment.is_payed = is_payed
    if is_pass is not None:
        if not enrollment.is_payed:
            raise HTTPException(400,"User has not completed payment")
        if enrollment.is_pass:
            raise HTTPException(400,"Candidate already marked as passed")
        enrollment.is_pass = is_pass
        enrollment.passed_at = datetime.utcnow()

    return update_enrollment(db, enrollment)
    