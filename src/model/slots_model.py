from sqlalchemy import Column,Date
from src.database.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

class Slot(Base):
    __tablename__="slots"
    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    slot=Column(Date,nullable=False)

    enroll=relationship("Enrollment",back_populates="slot")
