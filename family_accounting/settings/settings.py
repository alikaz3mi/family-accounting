from family_accounting import DEFAULT_PATH
from family_accounting.settings import DBSettings

db_settings = DBSettings(_env_file=f"{DEFAULT_PATH}/.env")
