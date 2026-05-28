from sqlalchemy.orm import Session
from src.repository.moc_repo import create_moc
from src.repository.enrollment_repo import get_enrollment_by_user
from src.repository.moc_repo import get_moc_by_userid_cycleno_document
from datetime import datetime
from src.utils.constants import PUNCTUAL,DANGEROUSLY_DELAYED,DELAYED,CYCLE_ONE,CYCLE_TWO,CYCLE_THREE
from src.utils.custom_Exceptions import EnrollmentNotFound,DocumentAlreadyExists,DocumentUploadfailed

def submit_document_service(db: Session, user_id, document, cycle_no):

        enrollment = get_enrollment_by_user(db, user_id)
        if not enrollment:
            raise EnrollmentNotFound()
        submitted_at = datetime.utcnow()
        print(submitted_at)
        print(enrollment.passed_at)
        total_years = ( submitted_at - enrollment.passed_at).days / 365 

        print(total_years)  
        current_cycle = None
        match total_years:
            case years if years < 3:
                current_cycle = CYCLE_ONE
            case years if years < 6:
                current_cycle = CYCLE_TWO
            case years if years < 9:
                current_cycle = CYCLE_THREE
        if cycle_no > current_cycle:
            raise DocumentUploadfailed()
        existing_document = get_moc_by_userid_cycleno_document(db,user_id,cycle_no,document)
        if existing_document:
            raise DocumentAlreadyExists()
        status = None
        match cycle_no:
            case 1:
                match total_years:
                    case years if years <= 3:
                        status = PUNCTUAL
                    case years if years > 3 and years <=4:
                        status = DELAYED
                    case _:
                        status = DANGEROUSLY_DELAYED
            case 2:
                match total_years:
                    case years if years <=6:
                        status = PUNCTUAL
                    case years if years > 6 and years <=7:
                        status = DELAYED
                    case _:
                        status = DANGEROUSLY_DELAYED
            case 3:
                match total_years:
                    case years if years <= 9:
                        status = PUNCTUAL
                    case years if years > 9 and years <=10:
                        status = DELAYED
                    case _:
                        status = DANGEROUSLY_DELAYED

        return create_moc(db=db,user_id=user_id,document=document,cycle_no=cycle_no,submitted_at=submitted_at,status=status)

      