import unittest
from family_accounting.entities import User


class TestUserEntity(unittest.TestCase):
    def test_user_creation(self):
        user = User(id=1, name="John Doe", phone="+1234567890", is_verified=True)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.phone, "+1234567890")
        self.assertTrue(user.is_verified)
        self.assertEqual(len(user.groups), 0)  # Default groups list is empty


if __name__ == "__main__":
    unittest.main()
