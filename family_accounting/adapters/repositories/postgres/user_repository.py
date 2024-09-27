from sqlalchemy.orm import Session
from family_accounting.entities import User as UserEntity
from family_accounting.adapters.database.models import UserModel
from family_accounting.use_cases.interfaces.user_repository_interface import UserRepositoryInterface
from family_accounting.utils.hashing import verify_password


class UserRepository(UserRepositoryInterface):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_by_phone(self, phone: str) -> UserEntity | None:
        user_record = self.db_session.query(UserModel).filter(UserModel.phone == phone).one_or_none()
        if user_record:
            return self._map_to_entity(user_record)
        return None

    def create_user(self, user: UserEntity) -> UserEntity:
        new_user = UserModel(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone,
            password=user.password,  # Assumed to be hashed before reaching here
            telegram_id=user.telegram_id,
            is_verified=user.is_verified,
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return self._map_to_entity(new_user)

    def update_user(self, user: UserEntity) -> None:
        existing_user = self.db_session.query(UserModel).filter(UserModel.id == user.id).one_or_none()
        if not existing_user:
            raise ValueError("User not found")

        existing_user.username = user.username
        existing_user.first_name = user.first_name
        existing_user.last_name = user.last_name
        existing_user.phone = user.phone
        existing_user.password = user.password  # Assumed to be hashed
        existing_user.telegram_id = user.telegram_id
        existing_user.is_verified = user.is_verified

        self.db_session.commit()

    def verify_password(self, phone: str, password: str) -> bool:
        user_record = self.db_session.query(UserModel).filter(UserModel.phone == phone).one_or_none()
        if not user_record:
            return False

        return verify_password(password, user_record.password)

    @staticmethod
    def _map_to_entity(user_record: UserModel) -> UserEntity:
        return UserEntity(
            id=user_record.id,
            username=user_record.username,
            first_name=user_record.first_name,
            last_name=user_record.last_name,
            phone=user_record.phone,
            password=user_record.password,
            telegram_id=user_record.telegram_id,
            is_verified=user_record.is_verified,
            groups=[],  # If groups are handled separately, you'll need to map them as well
        )
