from family_accounting.use_cases.interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from family_accounting.use_cases.interfaces.otp_service_interface import (
    OTPServiceInterface,
)


class LoginUseCase:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        otp_service: OTPServiceInterface,
    ):
        self.user_repository = user_repository
        self.otp_service = otp_service

    def execute(self, phone: str, password: str = None, otp_code: str = None) -> bool:
        # Fetch the user by phone number
        user = self.user_repository.find_by_phone(phone)
        if not user:
            raise ValueError("User not found")

        # If password is provided, verify password
        if password:
            if self.user_repository.verify_password(phone, password):
                return True
            else:
                raise ValueError("Invalid password")

        # If OTP code is provided, verify the OTP
        if otp_code:
            if self.otp_service.verify_otp(phone, otp_code):
                return True
            else:
                raise ValueError("Invalid OTP code")

        # If neither password nor OTP is provided, raise an error
        raise ValueError("Either password or OTP code must be provided")
