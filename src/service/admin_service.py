from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.repository.admin_repo import create_admin
from src.repository.role_repo import get_role_by_name
from src.repository.user_role_repo import assign_role
from src.repository.user_repo import get_user_by_email

from src.utils.hash import hash_password


def create_admin_service(
    db: Session,
    salutation: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str
):

    # Check existing user
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(
            400,
            "User already exists"
        )

    # Hash password
    hashed_password = hash_password(password)

    # Create admin
    admin = create_admin(
        db,
        salutation,
        first_name,
        last_name,
        email,
        hashed_password
    )

    # Get admin role
    admin_role = get_role_by_name(
        db,
        "admin"
    )

    # Assign role
    if admin_role:

        assign_role(
            db,
            admin.id,
            admin_role.id
        )

    return admin

def assign_admin_service(
    db: Session,
    user_id
):

    # Check user exists
    user = get_user_by_id(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            404,
            "User not found"
        )

    # Get admin role
    admin_role = get_role_by_name(
        db,
        "admin"
    )

    if not admin_role:

        raise HTTPException(
            404,
            "Admin role not found"
        )

    # Check already admin
    for role in user.roles:

        if role.name == "admin":

            raise HTTPException(
                400,
                "User already admin"
            )

    # Assign admin role
    assign_role(
        db,
        user.id,
        admin_role.id
    )

    return user