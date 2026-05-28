from pydantic import BaseModel, EmailStr, Field, field_validator
from fastapi import Form
from enum import Enum
import re


class Salutation(str, Enum):
    MR = "MR"
    MRS = "MRS"
    DR = "DR"
    MISS = "MISS"


class AdminCreate(BaseModel):
    salutation: Salutation = Form(...)
    first_name: str = Field(..., min_length=2, max_length=15)
    last_name: str = Field(..., min_length=2, max_length=15)
    email: EmailStr = Form(...)
    password: str = Field(..., min_length=6, max_length=15)

    @field_validator("first_name")
    def validate_first_name(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("First name should contain alphabets only")
        return v

    @field_validator("last_name")
    def validate_last_name(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("Last name should contain alphabets only")
        return v

    @field_validator("password")
    def validate_password(cls, v):
        if not re.search("[A-Z]", v):
            raise ValueError("Password must contain uppercase")

        if not re.search("[a-z]", v):
            raise ValueError("Password must contain lowercase")

        if not re.search("[0-9]", v):
            raise ValueError("Password must contain digit")

        return v
    
