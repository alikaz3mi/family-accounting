from abc import ABC, abstractmethod
from family_accounting.entities import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_by_phone(self, phone: str) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass

    @abstractmethod
    def verify_password(self, phone: str, password: str) -> bool:
        pass
