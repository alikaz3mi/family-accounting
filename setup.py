import logging
import re
import subprocess
from pathlib import Path
from typing import List

from setuptools import setup, find_packages

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()

logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def post_install():
    """Implement post installation routine"""
    with open("./requirements.txt") as f:
        install_requires = f.read().splitlines()

    install_requires = check_requirements(install_requires)

    return install_requires


def check_requirements(install_requires: List[str]):
    installed_pacakges_idx = []
    for idx, package in enumerate(install_requires):
        if "git" in package or "--" in package:
            result = subprocess.run(
                f"pip install {package}",
                shell=True,
                capture_output=True,
                text=True,
            )
            logger.info(f"{result.stdout}")
            if result.stderr != "":
                logger.error(f"{result.stderr}")
            installed_pacakges_idx.append(idx)
    for idx in installed_pacakges_idx:
        install_requires[idx] = ""
    install_requires = [x for x in install_requires if x != ""]
    return install_requires


def install_extra_requires(packages: List[str]):
    return check_requirements(packages)


def get_version():
    file = Path("./family_accounting/__init__.py")
    return re.search(
        r'^__version__ *= *[\'"]([^\'"]*)[\'"]',
        file.read_text(encoding="utf-8"),
        re.M,
    )[1]


setup(
    name="family_accounting",
    version=get_version(),
    url="git@github.com:alikaz3mi/family-accounting.git",
    description=" ",  # TODO: Short description of this project
    zip_safe=False,
    packages=find_packages(),
    install_requires=post_install(),
    entry_points={
        "console_scripts": ["family_accounting = family_accounting.__main__:main"],
    },
)
