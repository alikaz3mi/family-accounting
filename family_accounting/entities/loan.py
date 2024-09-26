from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class Loan(BaseModel):
    loan_id: int = Field(None, description="Unique ID for each loan")
    user_id: int = Field(None, description="ID of the user who applied for the loan")
    amount: float = Field(None, gt=0, description="Total loan amount")
    due_date: date = Field(None, description="Due date for the loan")
    status: str = Field(
        None,
        description="Current status of the loan (e.g., 'pending', 'approved', 'paid')",
    )
    payment_plan: Optional[str] = Field(None, description="Payment plan information")

    class Config:
        orm_mode = True
