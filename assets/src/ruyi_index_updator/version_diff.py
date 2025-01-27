"""
This checks if the version of each image needs to be updated, and if so, updates the version of the image.
"""

import os
import logging
import shutil
import tempfile
import hashlib
import toml
import traceback

from awesomeversion import AwesomeVersion

from ..ruyi_index_parser import PackageIndexProc, clone_package_index, BoardImages
from ..version_checker import gen_oldver
from ..matrix_parser import Systems, ImageStatus
from ..version_checker import VInfo
from .plugin_handler import find_plugin
from .upload_plugin_base import UploadPluginBase

logger = logging.getLogger(__name__)

CACHE_DIR: str | None = os.environ.get("CACHE_DIR", None)


def cmp_version(v1: str, v2: str) -> int:
    """
    Compare the version of two strings
    """
    av1 = AwesomeVersion(v1)
    av2 = AwesomeVersion(v2)
    if av1 > av2:
        return 1
    if av1 < av2:
        return -1
    return 0


class BoardImageWrapper:
    """
    Hold the operations on the board image index
    """

    def __init__(self,
                 vinfo: VInfo,
                 plugin: UploadPluginBase,
                 index_name: str,
                 old_indexs: list[BoardImages]
                 ):
        self.vinfo = vinfo
        self.plugin = plugin
        self.index_name = index_name
        self.old_indexs = old_indexs

        self.index = self.plugin.handle_report(
            self.vinfo, self.index_name, self.old_indexs)

    def new_index(self) -> BoardImages:
        """
        Generate the new index
        """
        return self.index

    def new_index_name(self) -> str:
        """
        Generate the new index file name
        """
        return f"{self.index.version}.toml"

    def new_index_dict(self) -> dict:
        """
        Generate the new index dict
        """
        return self.index.info.serialize()

    def new_index_toml(self) -> str:
        """
        Generate the new index toml
        """
        return toml.dumps(self.new_index_dict())

    def gen_hash(self) -> str:
        """
        Generate the hash of the new index, used to identify the pr
        """
        h = hashlib.sha224(
            self.new_index_toml().encode("utf-8") + self.new_index_name().encode("utf-8")
        )
        return h.hexdigest()


class RuyiDiff:
    """
    A wrapper for RuyiDiff, holding the resource, doing the diff process
    """

    tmp_path = None

    def __get_tmp_path(self):
        if self.tmp_path is not None:
            return
        if CACHE_DIR is not None:
            self.tmp_path = CACHE_DIR
        self.tmp_path = tempfile.mkdtemp()

    def __release_tmp_path(self):
        if self.tmp_path is None:
            return
        if CACHE_DIR is None:
            shutil.rmtree(self.tmp_path)

    def __yield_one_sys(self, vinfo: VInfo,
                        plug: UploadPluginBase, force: bool):
        for index_name, index in self.index.items():
            if not plug.is_mapped_ruyi_index(vinfo, index_name):
                continue
            newest_index = index[0]
            for i in index:
                if cmp_version(i.version, newest_index.version) > 0:
                    newest_index = i
            matrix_version = plug.handle_version(vinfo)
            logger.info("Handling index %s:%s:%s-%s:%s",
                        vinfo.vendor, vinfo.system, vinfo.variant, vinfo.version, matrix_version)
            if newest_index.version < matrix_version:
                logger.info(
                    "Find new version for %s: %s -> %s",
                    index_name, newest_index.version, matrix_version)
                yield BoardImageWrapper(vinfo, plug, index_name, index)
            elif force:
                logger.info(
                    "Force update for %s: %s -> %s",
                    index_name, newest_index.version, matrix_version)
                yield BoardImageWrapper(vinfo, plug, index_name, index)

    def gen_diff(self, filter_plugins: list[str] = None, threadhold=ImageStatus("basic"), force=False):
        """
        Yield the system that needs to be updated
        """
        for _, v in self.oldver.items():
            # Find the plugin that can handle the system
            plugin = find_plugin(v)
            if plugin is None:
                continue
            if filter_plugins is not None and len(filter_plugins) > 0 and \
                    plugin.get_name() not in filter_plugins:
                continue

            if v.raw_data.status < threadhold:
                continue

            # Please notice:
            # One system may have multiple ruyi_index, we need to handle them all
            # So, we need to iterate the index

            try:
                yield from self.__yield_one_sys(v, plugin, force)
            except Exception as e:
                logger.error("Error occurs when handling system %s:%s:%s-%s",
                             v.vendor, v.system, v.variant, v.version)
                logger.error("Error: %s", e)
                logger.error(traceback.format_exc())

    def __init__(self, matrix: Systems, conf: str):
        self.__get_tmp_path()
        index_path = os.path.join(self.tmp_path, "packages-index")
        self.repo = clone_package_index(index_path)
        self.index_proc = PackageIndexProc(index_path)
        self.index = self.index_proc.parse_board()
        self.matrix = matrix
        self.oldver = gen_oldver(matrix, conf)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__release_tmp_path()
