from family_accounting.entities import User
from family_accounting.use_cases.interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from pydantic import ValidationError


class RegistrationUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, phone: str, username: str, telegram_id: str = None) -> User:
        # Check if the user already exists by phone number
        existing_user = self.user_repository.find_by_phone(phone)
        if existing_user:
            raise ValueError("User with this phone number already exists")

        # Create a new user entity
        try:
            new_user = User(
                username=username,
                phone=phone,
                telegram_id=telegram_id,
                is_verified=False,
            )
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")

        created_user = self.user_repository.create_user(new_user)
        return created_user
