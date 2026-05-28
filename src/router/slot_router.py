from fastapi import APIRouter,HTTPException,Depends,Form
from typing import Annotated
from sqlalchemy.orm import Session
from src.schema.slot_schema import CreateSlot,SlotResponse
from src.database.session import get_db
from src.service.slot_service import create_slot_service,get_all_slots_service
from src.utils.logger import logger
from src.dependencies.role_dependency import require_role


router = APIRouter(prefix="/slot", tags=["Slot"])

@router.post("/create_slot",response_model=SlotResponse)
def create_slot(data:Annotated[CreateSlot, Form()],db:Session=Depends(get_db),current_user = Depends(require_role("candidate","admin"))):
    try:
        return create_slot_service(data.slot,db)  
    except HTTPException:
        raise
    except Exception as e:
        logger.info(f"route erorr {str(e)}")
        raise HTTPException(500,"Internal Server Error")
    

@router.get("/",response_model=list[SlotResponse])
def get_all_slots(db:Session=Depends(get_db)):
    try:
        return get_all_slots_service(db)
    except Exception as e:
        logger.error(f"get all slots error:{str(e)}")
        raise HTTPException(500,"Internal Server Error")

    
