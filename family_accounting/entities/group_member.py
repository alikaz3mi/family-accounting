from pydantic import BaseModel, Field
from typing import Optional, Literal

from enum import Enum


class AccessLevel(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class GroupMember(BaseModel):
    group_member_id: int = Field(None, description="Unique ID for each group member")
    group_id: int = Field(None, description="ID of the group")
    user_id: int = Field(
        None,
        description="ID of the user associated with the group member",
    )
    access_level: Literal[
        AccessLevel.OWNER,
        AccessLevel.ADMIN,
        AccessLevel.MEMBER,
    ] = Field(None, description="Access level for the group member")
    role: Optional[str] = Field(
        None,
        description="Optional description of the member's role",
    )

    class Config:
        orm_mode = True
