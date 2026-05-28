from sqlalchemy import Column,String,Integer
from src.database.base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from src.model.user_role_model import user_roles
class User(Base):
    __tablename__="users"
    id=Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    salutation=Column(String,nullable=False)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    degree=Column(String,nullable=True)
    degree_certificate=Column(String,nullable=True)
    passing_year=Column(Integer,nullable=True)
    email=Column(String,unique=True,nullable=False)
    password_hash=Column(String,nullable=False)

    enroll=relationship("Enrollment",back_populates="user")
    roles = relationship("Role",secondary=user_roles,back_populates="users")
    mocs = relationship("MOC", back_populates="user")