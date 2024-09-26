from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

from family_accounting.entities.group_member import GroupMember


class User(BaseModel):
    id: int = Field(..., description="User unique ID")
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Full name of the user",
    )
    phone: str = Field(
        ...,
        pattern=r"^\+?\d{10,15}$",
        description="Phone number of the user",
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
