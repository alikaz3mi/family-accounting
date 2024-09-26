from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Transaction(BaseModel):
    transaction_id: int = Field(None, description="Unique transaction ID")
    loan_id: Optional[int] = Field(None, description="Associated loan ID if applicable")
    user_id: int = Field(None, description="ID of the user who made the transaction")
    amount: float = Field(None, gt=0, description="Amount of the transaction")
    payment_type: str = Field(
        None,
        description="Payment type (e.g., 'installment', 'loan payment')",
    )
    receipt_url: Optional[str] = Field(None, description="URL of the uploaded receipt")
    receipt_verified: bool = Field(False, description="Whether the receipt is verified")
    date_time: datetime = Field(None, description="Date and time of the transaction")

    class Config:
        orm_mode = True
