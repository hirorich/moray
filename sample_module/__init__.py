"""
https://blog.hiros-dot.net/?p=10328
"""

import logging
from logging import FileHandler, Formatter, DEBUG, INFO, ERROR
from pathlib import Path

_UTF_8 = 'utf-8'

_log_folder = Path('log')
_debug_log = _log_folder.joinpath('moray_debug.log')
_info_log = _log_folder.joinpath('moray_info.log')
_error_log = _log_folder.joinpath('moray_error.log')
if not _log_folder.exists():
    _log_folder.mkdir()

_format = '[%(asctime)s][%(levelname)s] %(message)s (at %(name)s:%(lineno)s)'
_formatter = Formatter(_format)

_debug_handler = FileHandler(_debug_log, encoding=_UTF_8)
_debug_handler.setLevel(DEBUG)
_debug_handler.setFormatter(_formatter)

_info_handler = FileHandler(_info_log, encoding=_UTF_8)
_info_handler.setLevel(INFO)
_info_handler.setFormatter(_formatter)

_error_handler = FileHandler(_error_log, encoding=_UTF_8)
_error_handler.setLevel(ERROR)
_error_handler.setFormatter(_formatter)

logger = logging.getLogger('moray')
logger.addHandler(_debug_handler)
logger.addHandler(_info_handler)
logger.addHandler(_error_handler)
logger.setLevel(DEBUG)
