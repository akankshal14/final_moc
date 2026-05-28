from fastapi import (
    APIRouter,
    Depends,
    Form,
    status
)

from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from typing import Annotated

from src.database.session import get_db

from src.schema.moc_schema import CreateMoc

from src.service.moc_service import (
    submit_document_service
)

from src.dependencies.role_dependency import (
    require_role
)

from src.utils.custom_Exceptions import (
    AppException
)

from src.utils.constants import (
    INTERNAL_SERVER_ERROR
)


router = APIRouter(
    prefix="/moc",
    tags=["MOC"]
)


@router.post("/")
def submit_document(
    data: Annotated[CreateMoc, Form()],
    db: Session = Depends(get_db),

    current_user = Depends(
        require_role("candidate")
    )
):

    try:

        user_id = current_user.get(
            "user_id"
        )

        result = submit_document_service(
            db,
            user_id,
            data.document,
            data.cycle_no
        )

        return result

    except AppException as e:
        print("hhhhh")
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": e.msg
            }
        )

    except Exception:

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": INTERNAL_SERVER_ERROR
            }
        )