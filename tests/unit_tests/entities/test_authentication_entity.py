import unittest
from family_accounting.entities import Authentication


class TestAuthenticationEntity(unittest.TestCase):
    def test_authentication_creation(self):
        auth = Authentication(user_id=1, phone="+1234567890", token="abc123")
        self.assertEqual(auth.user_id, 1)
        self.assertEqual(auth.phone, "+1234567890")
        self.assertEqual(auth.token, "abc123")


if __name__ == "__main__":
    unittest.main()
