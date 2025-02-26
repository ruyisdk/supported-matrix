# pylint: disable=import-outside-toplevel
"""
Base class for upload plugins. 

**NOTICE** You shall use dynamic import in the plugin handler.

See lm4a_revy.py for example.
"""

from abc import ABC, abstractmethod
from ..matrix_parser import VInfo
from .ruyi_index_parser import BoardImages, DistfileDeclType


class UploadPluginBase(ABC):
    """
    A base interface for plugins
    """
    __version__: str = None
    __tmppath__: str = None

    import logging

    def __init__(self) -> None:
        self.logger = self.logging.getLogger("ruyi_index_updator")

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        """
        Get the name of the plugin
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Ruyi Index Updator Plugin: {self.get_name()}: v{self.__version__}>"

    @abstractmethod
    def can_handle(self, vinfo: VInfo) -> bool:
        """
        Check if the plugin can handle a system from support matrix
        """
        raise NotImplementedError

    def all_index_can_handle(self) -> dict[str, tuple[str, str, str]]:
        """
        Give a list of all the index name from packages index which this plugin can process.
        This is not necessary, but better have it to allow extra checker applyed.
        """
        return {}

    @abstractmethod
    def is_mapped_ruyi_index(self, vinfo: VInfo, index: str) -> bool:
        """
        Check if the ruyi index is mapped from the system.
        """
        raise NotImplementedError

    @abstractmethod
    def handle_version(self, vinfo: VInfo) -> str:
        """
        Handle the version mapping from system version to Ruyi Index version.
        """
        raise NotImplementedError

    @abstractmethod
    def handle_report(self, vinfo: VInfo,
                      index: str, last_index: list[BoardImages]) -> BoardImages | None:
        """
        Handle the report data from the system.
        """
        raise NotImplementedError

    # Helper functions

    import os
    import requests
    from tqdm import tqdm
    import hashlib
    import copy
    from awesomeversion import AwesomeVersion
    import urllib.parse as urllib_parse

    def cmp_version(self, v1: str, v2: str) -> int:
        """
        Compare the version of two strings
        Though this function is in version_diff.py, as plugins runs in a seprate env, we need to rewrite it here.
        """
        av1 = self.AwesomeVersion(v1)
        av2 = self.AwesomeVersion(v2)
        if av1 > av2:
            return 1
        if av1 < av2:
            return -1
        return 0

    def download_file(self, file: str, url: str) -> str:
        """
        Download a file from the internet url, save it to file. 
        """
        if self.os.path.exists(file):
            self.logger.info(
                "File %s already exists, skipping download.", file)
            return file
        chunk_size = 4096
        resp = self.requests.get(url, stream=True, timeout=60)
        tot_sz = int(resp.headers.get("content-length", 0))
        self.logger.info("Downloading %s to %s", url, file)
        with self.tqdm(total=tot_sz, unit="B", unit_scale=True) as pbar:
            with open(file, 'wb') as f:
                for chunk in resp.iter_content(chunk_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
        return file

    def file_size(self, file: str) -> int:
        """
        Get the size of a file.
        """
        return self.os.path.getsize(file)

    def urljoin(self, base: str, path: str) -> str:
        """
        Do a urljoin
        """
        return self.urllib_parse.urljoin(base + '/', path)

    def urlbasename(self, url: str) -> str:
        """
        Get the basename of a url.
        """
        parsed = self.urllib_parse.urlparse(url)
        path = parsed.path
        if path and path.endswith('/'):
            return ""
        filename = self.os.path.basename(path)
        return filename

    def sha256sum(self, file: str) -> str:
        """
        Calculate the sha256sum of a file.
        """
        sha256 = self.hashlib.sha256()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def sha512sum(self, file: str) -> str:
        """
        Calculate the sha512sum of a file.
        """
        sha512 = self.hashlib.sha512()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha512.update(chunk)
        return sha512.hexdigest()

    def gen_distfile(self, file: str, url: str) -> DistfileDeclType:
        """
        Generate a distfile object from a file.
        """
        return {
            "name": self.os.path.basename(file),
            "size": self.file_size(file),
            "urls": [url],
            "checksums": {
                "sha256": self.sha256sum(file),
                "sha512": self.sha512sum(file),
            },
            "restrict": ["mirror"],
        }

    def autoupdate_index(self, last_index: BoardImages, vinfo: VInfo,
                         desc: str, distfiles: dict[str, DistfileDeclType]) -> BoardImages:
        """
        Auto update the index.
        """
        res = self.copy.copy(last_index)
        res.is_bot_created = True
        res.version = self.handle_version(vinfo)
        res.info["metadata"]["desc"] = desc
        res.info["distfiles"] = list(distfiles.values())
        res.info["blob"]["distfiles"] = [
            dist["name"] for dist in distfiles.values()
        ]
        res.info["provisionable"]["partition_map"] = {
            k: ".".join(v["name"].split(".")[:-1]) for k, v in distfiles.items()
        }
        return res


def register() -> UploadPluginBase | None:
    """
    Register the plugin to the system
    **Required to be implemented in the plugin**
    """
    return None
