from pydantic import BaseModel, Field
from typing import Optional


class Authentication(BaseModel):
    user_id: int = Field(
        None,
        description="User ID associated with this authentication session",
    )
    phone: str = Field(
        None,
        pattern=r"^\+?\d{10,15}$",
        description="Phone number for authentication",
    )
    sms_code: Optional[str] = Field(None, description="SMS code for verification")
    telegram_id: Optional[str] = Field(
        None,
        description="Optional Telegram ID for login",
    )
    token: str = Field(None, description="Authentication token")

    class Config:
        orm_mode = True
