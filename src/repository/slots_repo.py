from sqlalchemy.orm import Session
from src.model.slots_model import Slot
from datetime import date
def create_slot(data,db:Session):
    slots=Slot(slot=data)
    db.add(slots)
    db.commit()
    db.refresh(slots)
    return slots

def get_all_slots(db: Session):
    return db.query(Slot).filter(Slot.slot > date.today()).all()