from fastapi import APIRouter,HTTPException,Depends,Form
from typing import Annotated
from sqlalchemy.orm import Session
from src.schema.admin_schema import AdminCreate
from src.database.session import get_db
from src.service.admin_service import create_admin_service
from src.utils.logger import logger
from src.schema.user_schema import AdminResponse
from src.dependencies.role_dependency import require_role
from uuid import UUID

router = APIRouter(prefix="/admin", tags=["Admin"])
@router.post("/create",response_model=AdminResponse)
def create_admin(user:Annotated[AdminCreate, Form()],db:Session=Depends(get_db), current_user = Depends(require_role("superadmin"))):
    try:

        return create_admin_service(
            db,
            user.salutation,
            user.first_name,
            user.last_name,
            user.email,
            user.password
        )

    except HTTPException:
        raise

    except Exception as e:

        logger.info(f"route error {str(e)}")

        raise HTTPException(
            500,
            "Internal Server Error"
        )



@router.post(
    "/assign-admin/{user_id}",
    response_model=AdminResponse
)
def assign_admin_role(
    user_id: UUID,
    db: Session = Depends(get_db),

    # Only superadmin allowed
    current_user = Depends(
        require_role("superadmin")
    )
):

    try:

        return assign_admin_service(
            db,
            user_id
        )

    except HTTPException:
        raise

    except Exception as e:

        logger.error(
            f"assign admin error {str(e)}"
        )

        raise HTTPException(
            500,
            "Internal Server Error"
        ) 