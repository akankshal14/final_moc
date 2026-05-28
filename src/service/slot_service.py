from sqlalchemy.orm import Session
from src.repository.slots_repo import create_slot,get_all_slots
from datetime import date
from src.utils.logger import logger

def create_slot_service(data:date,db:Session):
    try:
        return create_slot(data,db)
    except Exception as e:
        logger.info(f"service error{str(e)}")
        raise e
    

def get_all_slots_service(db:Session):
    try:
        return get_all_slots(db)
    except Exception as e:
        logger.error(f"get all slot service error{str(e)}")
        raise e
