try:
    from pip._internal.utils.typing import MYPY_CHECK_RUNNING
except ModuleNotFoundError:
    MYPY_CHECK_RUNNING = False

if MYPY_CHECK_RUNNING:
    from typing import List, Optional


def main(args=None):
    # type: (Optional[List[str]]) -> int
    """This is preserved for old console scripts that may still be referencing
    it.
    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
