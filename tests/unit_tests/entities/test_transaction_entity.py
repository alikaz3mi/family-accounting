import unittest
from datetime import datetime
from family_accounting.entities import Transaction


class TestTransactionEntity(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(
            transaction_id=202,
            user_id=1,
            amount=150.0,
            payment_type="installment",
            date_time=datetime(2024, 9, 25),
        )
        self.assertEqual(transaction.transaction_id, 202)
        self.assertEqual(transaction.user_id, 1)
        self.assertEqual(transaction.amount, 150.0)
        self.assertEqual(transaction.payment_type, "installment")
        self.assertEqual(transaction.date_time, datetime(2024, 9, 25))


if __name__ == "__main__":
    unittest.main()
