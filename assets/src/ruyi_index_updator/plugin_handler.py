"""
Plugin handler module
"""

import os
import logging
from functools import partial
from pluginbase import PluginBase

from .config import config
from . import util
from .upload_plugin_base import UploadPluginBase
from ..version_checker import VInfo

logger = logging.getLogger(__name__)

pwd = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, pwd)
plugin_base = PluginBase(package="src.ruyi_index_updator.plugins")

plugins: list[UploadPluginBase] = []

def load_all_plugins():
    """
    Load all plugins
    """
    sources = plugin_base.make_plugin_source(
        searchpath=[get_path("./upload_plugin")],
    )

    tmp_path = util.folder_tmp_mux(config["CACHE_DIR"])

    for plugin_name in sources.list_plugins():
        if plugin_name == "prelude":
            continue
        plugin = sources.load_plugin(plugin_name)  # Typing magic
        plug: UploadPluginBase | None = plugin.register()
        if plug is None:
            continue
        t_path = os.path.join(tmp_path, plug.get_name())
        os.makedirs(t_path, exist_ok=True)
        plug.__version__ = plugin.__version__
        plug.__tmppath__ = t_path
        plugins.append(plug)


def find_plugin(vinfo: VInfo) -> UploadPluginBase | None:
    """
    Find the plugin that can handle the system
    """
    for plugin in plugins:
        if plugin.can_handle(vinfo):
            return plugin
    return None


def __init__():
    if not plugins or len(plugins) == 0:
        load_all_plugins()


__init__()
