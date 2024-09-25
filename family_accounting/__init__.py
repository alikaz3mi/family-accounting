__version__ = "0.0.1"
__name__ = "family_accounting"

import os
from pathlib import Path
from ai_utils import simple_logger


DEFAULT_PATH = Path(os.path.realpath(__file__)).parents[1]
LOGGER = simple_logger(__name__)


__all__ = [
    "__version__",
    "LOGGER",
    "DEFAULT_PATH",
]
