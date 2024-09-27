import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from family_accounting.adapters.database.models import Base, UserModel
from family_accounting.adapters.repositories.postgres.user_repository import UserRepository
from family_accounting.entities import User as UserEntity
from family_accounting.utils.hashing import get_password_hash


class TestUserRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up in-memory SQLite database and session for the tests."""
        cls.engine = create_engine("sqlite:///:memory:", echo=False)
        Base.metadata.create_all(cls.engine)  # Create tables in the in-memory database
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        """Create a new session for each test."""
        self.session = self.Session()
        self.user_repository = UserRepository(self.session)

    def tearDown(self):
        """Rollback any changes and close the session after each test."""
        self.session.rollback()
        self.session.close()

    def test_create_user(self):
        """Test creating a new user and fetching them from the database."""
        user_entity = UserEntity(
            username="John Doe",
            phone="+1234567891",
            password=get_password_hash("password123"),
            is_verified=False,
            telegram_id="john_doe_telegram"
        )

        # Test the creation of a new user
        created_user = self.user_repository.create_user(user_entity)
        self.assertIsNotNone(created_user.id)  # Ensure the user ID is set after creation
        self.assertEqual(created_user.username, "John Doe")
        self.assertEqual(created_user.phone, "+1234567891")

        # Now fetch the user and check again
        fetched_user = self.user_repository.find_by_phone("+1234567891")
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.username, "John Doe")
        self.assertEqual(fetched_user.phone, "+1234567891")

    def test_find_by_phone(self):
        """Test finding an existing user by their phone number."""
        # First, create a user
        user_entity = UserEntity(
            username="Jane Doe",
            phone="+9876543210",
            password=get_password_hash("password456"),
            is_verified=True,
            telegram_id="jane_doe_telegram"
        )
        self.user_repository.create_user(user_entity)

        # Test finding the user
        fetched_user = self.user_repository.find_by_phone("+9876543210")
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.username, "Jane Doe")
        self.assertTrue(fetched_user.is_verified)

        # Test finding a non-existent user
        non_existent_user = self.user_repository.find_by_phone("+98716543210")
        self.assertIsNone(non_existent_user)

    def test_verify_password(self):
        """Test verifying a user's password."""
        hashed_password = get_password_hash("securepassword")
        user_entity = UserEntity(
            username="Password Tester",
            phone="+1999999999",
            password=hashed_password,
            is_verified=True,
            telegram_id=None
        )
        self.user_repository.create_user(user_entity)

        # Correct password
        is_valid = self.user_repository.verify_password("+1999999999", "securepassword")
        self.assertTrue(is_valid)

        # Incorrect password
        is_invalid = self.user_repository.verify_password("+9999999399", "wrongpassword")
        self.assertFalse(is_invalid)

    def test_update_user(self):
        """Test updating a user's information."""
        # First, create a user
        user_entity = UserEntity(
            username="Update Tester",
            phone="+1555555555",
            password=get_password_hash("updatepassword"),
            is_verified=False,
            telegram_id="update_tester"
        )
        created_user = self.user_repository.create_user(user_entity)

        # Update the user information
        created_user.username = "Updated Name"
        created_user.is_verified = True
        self.user_repository.update_user(created_user)

        # Fetch the updated user
        updated_user = self.user_repository.find_by_phone("+1555555555")
        self.assertEqual(updated_user.username, "Updated Name")
        self.assertTrue(updated_user.is_verified)


if __name__ == "__main__":
    unittest.main()
