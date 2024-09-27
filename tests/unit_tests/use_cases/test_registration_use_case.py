import unittest
from unittest.mock import Mock
from family_accounting.use_cases.registration_use_case import RegistrationUseCase
from family_accounting.entities import User


class TestRegistrationUseCase(unittest.TestCase):
    def setUp(self):
        self.user_repository = Mock()
        self.use_case = RegistrationUseCase(user_repository=self.user_repository)

    def test_successful_registration(self):
        # Setup the mock repository
        self.user_repository.find_by_phone.return_value = None
        self.user_repository.create_user.return_value = User(
            id=1,
            username="John Doe",
            phone="+1234567891",
            telegram_id=None,
            is_verified=False,
        )

        # Execute the use case
        user = self.use_case.execute(phone="+1234567891", username="John Doe")

        # Assert the correct user was created
        self.user_repository.create_user.assert_called_once()
        self.assertEqual(user.username, "John Doe")

    def test_registration_with_existing_user(self):
        # Setup the mock to return an existing user
        self.user_repository.find_by_phone.return_value = User(
            id=1,
            name="John Doe",
            phone="+1234567891",
            telegram_id=None,
            is_verified=False,
        )

        # Attempt registration and expect an exception
        with self.assertRaises(ValueError):
            self.use_case.execute(phone="+1234567891", username="John Doe")


if __name__ == "__main__":
    unittest.main()
