from pydantic import BaseModel,field_validator
from fastapi import Form
from datetime import date,timedelta
from uuid import UUID

class CreateSlot(BaseModel):
    slot:date=Form(...)

    @field_validator("slot")
    def validate_slot_date(cls, slot_date:date):
        if slot_date < date.today():
            raise ValueError("Slot date cannot be in the past")

        if slot_date == date.today():
            raise ValueError("Slot date cannot be today")

        if slot_date > date.today() + timedelta(days=365):
            raise ValueError("Slot date cannot be more than 1 year")

        return slot_date

class SlotResponse(BaseModel):
    id:UUID
    slot:date
    