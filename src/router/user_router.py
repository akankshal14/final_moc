from fastapi import APIRouter,HTTPException,Depends,Form
from typing import Annotated
from sqlalchemy.orm import Session
from src.schema.user_schema import UserCreate,TokenResponse,UserLogin,UserResponse
from src.database.session import get_db
from src.service.user_service import register_user,login_user
router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register",response_model=UserResponse)
def register(user:Annotated[UserCreate, Form()],db:Session=Depends(get_db)):
    try:
        return register_user(db,user.salutation,user.first_name,user.last_name,user.degree,user.degree_certificate,user.passing_year,user.email, user.password) 
        
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(500,"Internal Server Error")
    
    
@router.post("/login", response_model=TokenResponse)
def login(user:Annotated[UserLogin, Form()], db: Session = Depends(get_db)):
    try:
        return login_user(db, user.email, user.password)
    
    except Exception as e:
        raise HTTPException(500,"Internal Server Error")
    
