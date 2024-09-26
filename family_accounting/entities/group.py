from pydantic import BaseModel, Field
from typing import List

from family_accounting.entities import GroupMember


class Group(BaseModel):
    group_id: int = Field(None, description="Unique group ID")
    name: str = Field(
        None,
        min_length=1,
        max_length=100,
        description="Name of the group",
    )
    owner_user_id: int = Field(
        None,
        description="ID of the user who is the group owner",
    )
    members: List[GroupMember] = Field([], description="List of group members")

    class Config:
        orm_mode = True
