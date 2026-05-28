from pydantic import BaseModel,EmailStr,Field,field_validator
from fastapi import Form
import re
from enum import Enum
from datetime import datetime

class Salutation(str,Enum):
    MR="MR"
    MRS="MRS"
    Dr="DR"
    Miss="MISS"

class Degree(str,Enum):
    MBBS="MBBS"
    BMS="BMS"
    BHMS="BHMS"

class UserCreate(BaseModel):
    salutation:Salutation=Form(...)
    first_name:str=Field(..., min_length=2, max_length=15)
    last_name:str=Field(..., min_length=4, max_length=15)
    degree:Degree=Form(...)
    degree_certificate:str=Form(...)
    passing_year:int=Form(...)
    email:EmailStr=Form(...)
    password:str=Field(..., min_length=6, max_length=15)
    
    @field_validator("first_name")
    def name_validaton(cls,n):
        if not n.strip():
            raise ValueError("Name can't be empty string")
        if not re.fullmatch(r"[A-Za-z ]+",n):
            raise ValueError("Name should contain alphabets only")
        return n
    
    @field_validator("last_name")
    def last_name_validaton(cls,n):
        if not n.strip():
            raise ValueError("Last Name can't be empty string")
        if not re.fullmatch(r"[A-Za-z ]+",n):
            raise ValueError("Last Name should contain alphabets only")
        return n

    @field_validator("password")
    def password_validation(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters")

        if not re.search("[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search("[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search("[0-9]", v):
            raise ValueError("Password must contain at least one digit")
        return v

    @field_validator("passing_year")
    def validate_passing_year(cls, passing_year):

        current_year = datetime.now().year

        if passing_year < 1926 or passing_year > current_year:
            raise ValueError(
                f"Passing year must be between 1900 and {current_year}"
            )

        return passing_year
    
class UserLogin(BaseModel):
    email:EmailStr=Form(...)
    password:str=Form(...)
    
class TokenResponse(BaseModel):
    user_id: str
    name:str
    surname:str
    roles:list[str]
    access_token:str
    refresh_token:str
    token_type:str ="bearer"

class UserResponse(BaseModel):
    salutation:Salutation
    first_name:str
    last_name:str
    degree:Degree
    degree_certificate:str
    passing_year:int
    email:EmailStr
    
class AdminResponse(BaseModel):
    salutation:Salutation
    first_name:str
    last_name:str
    email:EmailStr
    

