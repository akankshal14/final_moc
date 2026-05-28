from pydantic import BaseModel
from uuid import UUID
from typing import Optional
class CreateEnrollment(BaseModel):
    slot_id:UUID
    candidate_id:UUID


class EnrollmentResponse(BaseModel):
    id:UUID
    slot_id:UUID
    candidate_id:UUID
    is_payed: bool
    is_pass: bool

class UpdateEnrollmentStatus(BaseModel):
    is_payed: Optional[bool] = None
    is_pass: Optional[bool] = None
