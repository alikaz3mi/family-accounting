from lagom import Singleton
from dependencies import container

from family_accounting.settings.settings import db_settings, DBSettings


def set_settings(container_object: container):
    container_object[DBSettings] = Singleton(db_settings)


def set_use_cases(container_object: container):
    pass


def set_frameworks(container_object: container):
    pass


def set_adapters(container_object: container):
    pass


def setup(container_object: container):
    set_settings(container_object)
    set_use_cases(container_object)
    set_frameworks(container_object)
    set_adapters(container_object)
    return container_object


setup(container)
