# pylint: disable=unused-import, wildcard-import, unused-wildcard-import
"""
Prelude for upload plugins.
"""

import logging
logger = logging.getLogger(__name__)

try:
    from src.ruyi_index_parser import *
    from src.version_checker import VInfo
    from src.ruyi_index_updater.upload_plugin_base import UploadPluginBase
except ModuleNotFoundError:
    # Things above is used for type hinting
    # when the module is used as a plugin, load will fail
    pass
