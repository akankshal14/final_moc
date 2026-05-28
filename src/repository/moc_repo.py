from sqlalchemy.orm import Session
from src.model.moc_model import MOC

def create_moc(db:Session, user_id,document,cycle_no,submitted_at,status):
    moc=MOC( user_id=user_id,document=document,cycle_no=cycle_no,submitted_at=submitted_at,status=status)
    db.add(moc)
    db.commit()
    db.refresh(moc)
    return moc

def get_moc_by_userid_cycleno_document(db: Session,user_id,cycle_no,document):
    return (db.query(MOC).filter(MOC.user_id == user_id,MOC.cycle_no == cycle_no,MOC.document == document).first())