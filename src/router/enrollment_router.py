from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.service.enrollment_service import enroll_user,update_enrollment_status
from src.utils.logger import logger
from src.schema.enrollment_schema import CreateEnrollment,EnrollmentResponse,UpdateEnrollmentStatus
from uuid import UUID
from src.utils.constants import INTERNAL_SERVER_ERROR

router = APIRouter(prefix="/enrollment",tags=["Enrollment"])
@router.post("/create",response_model=EnrollmentResponse)
def create_enroll(data:CreateEnrollment,db: Session = Depends(get_db)):
    try:
        return enroll_user(db,data.slot_id,data.candidate_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"create enroller error{str(e)}")
        raise HTTPException(500,"Internal Server Error")
    
@router.patch("/{enrollment_id}")
def update_enrollment(enrollment_id: UUID,data: UpdateEnrollmentStatus,db: Session = Depends(get_db)):
    try:
        return update_enrollment_status(db=db,enrollment_id=enrollment_id,is_payed=data.is_payed,is_pass=data.is_pass)
    except HTTPException:
        raise
    except Exception as e: 
        logger.error(f"update enrollment error{str(e)}")
        raise HTTPException(500,INTERNAL_SERVER_ERROR)
