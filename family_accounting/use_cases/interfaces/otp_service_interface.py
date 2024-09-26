from abc import ABC, abstractmethod


class OTPServiceInterface(ABC):
    @abstractmethod
    def send_otp(self, phone: str) -> None:
        pass

    @abstractmethod
    def verify_otp(self, phone: str, otp_code: str) -> bool:
        pass
