import unittest
from datetime import date
from family_accounting.entities import Loan


class TestLoanEntity(unittest.TestCase):
    def test_loan_creation(self):
        loan = Loan(
            loan_id=101,
            user_id=1,
            amount=5000.0,
            due_date=date(2024, 12, 1),
            status="pending",
        )
        self.assertEqual(loan.loan_id, 101)
        self.assertEqual(loan.user_id, 1)
        self.assertEqual(loan.amount, 5000.0)
        self.assertEqual(loan.due_date, date(2024, 12, 1))
        self.assertEqual(loan.status, "pending")


if __name__ == "__main__":
    unittest.main()
