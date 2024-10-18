from family_accounting import LOGGER
from family_accounting.config_dependency_injection import container


def main():
    LOGGER.info("Welcome to Family Accounting")
    LOGGER.info(f"{container}")


if __name__ == "__main__":
    main()
