"""
Update new config to ruyi_index automatically
"""

import os
import logging
import colorlog

from .config import config
from .version_diff import RuyiDiff
from .index_handler import RuyiGitRepo

def _init_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s[%(relativeCreated)d %(levelname)s]%(reset)s: %(message)s'))

    handlers = [handler]

    if config["log"] is not None:
        p = os.path.abspath(config["log"])
        log_handler = logging.FileHandler(p)
        log_handler.setFormatter(logging.Formatter(
            '%(relativeCreated)d %(levelname)s: %(message)s'))
        log_handler.setLevel(logging.INFO)
        handlers.append(log_handler)

    if config["warn"] is not None:
        p = os.path.abspath(config["warn"])
        warn_handler = logging.FileHandler(p)
        warn_handler.setFormatter(logging.Formatter(
            '%(relativeCreated)d %(levelname)s: %(message)s'))
        warn_handler.setLevel(logging.WARNING)
        handlers.append(warn_handler)

    logging.basicConfig(level=logging.INFO, handlers=handlers)

_init_logger()
