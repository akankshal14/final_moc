import uuid
from sqlalchemy import Column,DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from src.database.base import Base
from sqlalchemy.orm import relationship


class MOC(Base):
    __tablename__ = "moc"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    document = Column(String,nullable=False)
    cycle_no = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")
    submitted_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="mocs")
    