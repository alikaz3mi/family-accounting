from ai_utils import simple_logger
from .. import __version__

logger = simple_logger(__name__)


def deprecation_warn(arg, new_arg, version=None):
    """Issue a deprecation warning when a deprecated argument is used, suggesting an updated argument."""
    if not version:
        version = float(__version__[:3]) + 0.2  # deprecate after 2nd major release
    logger.warning(
        f"WARNING ⚠️ '{arg}' is deprecated and will be removed in 'family_accounting {version}' in the future. "
        f"Please use '{new_arg}' instead.",
    )
