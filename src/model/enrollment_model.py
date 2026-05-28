from sqlalchemy import Column,ForeignKey,Boolean,DateTime
from src.database.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__="enrollment"
    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    slot_id=Column(UUID(as_uuid=True),ForeignKey("slots.id"),nullable=False)
    candidate_id=Column(UUID(as_uuid=True),ForeignKey("users.id"),nullable=False)
    is_payed=Column(Boolean,default=False)
    is_pass=Column(Boolean,default=False)
    passed_at = Column(DateTime, nullable=True)
    user=relationship("User",back_populates="enroll")
    slot=relationship("Slot",back_populates="enroll")
    
