from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from family_accounting.entities.group_member import GroupMember


class User(BaseModel):
    id: int = Field(None, description="User unique ID")
    username: Optional[str] = Field(
        None,
        min_length=3,
        max_length=50,
        description="Optional username for the user, unique within the system",
    )
    first_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="First name of the user",
    )
    last_name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Last name of the user",
    )
    phone: str = Field(
        None,
        pattern=r"^\+?\d{10,15}$",
        description="Phone number of the user",
    )
    password: Optional[str] = Field(
        None,
        description="Hashed password for the user",
    )
    telegram_id: Optional[str] = Field(None, description="Telegram ID for login")
    email: Optional[EmailStr] = Field(None, description="Optional email address")
    is_verified: bool = Field(False, description="Verification status of the user")
    groups: List[GroupMember] = Field(
        [],
        description="List of groups the user belongs to",
    )

    class Config:
        orm_mode = True
