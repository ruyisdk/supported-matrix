# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
"""
Handle most common image comes from github release
"""

from dataclasses import dataclass
from .prelude import *

__version__ = "0.0.1"


@dataclass
class HandleInfo:
    from typing import Callable
    index: str
    tup: tuple[str, str, str]
    version_mapper: Callable[[VInfo], str]
    repo: str
    release_filter: Callable[[VInfo, str], bool]
    asset_filter: Callable[[VInfo, str], bool]
    gen_desc: Callable[[VInfo, str], str]


class GithubReleaseGetter(UploadPluginBase):

    @staticmethod
    def get_name() -> str:
        return "github_release_getter"

    can_handle_lst: list[HandleInfo]

    # In handel version, we need to know which index we are handling.
    # In design, a single plugin should handle only one index.
    # So we need to pass the index to the function.
    cur_index: str

    def find_handler(self):
        for handle_info in self.can_handle_lst:
            if handle_info.index == self.cur_index:
                return handle_info
        raise ValueError("No handler found")

    def __init__(self, _can_handle: list[HandleInfo]):
        super().__init__()
        self.can_handle_lst = _can_handle
        self.cur_index = ""

    def can_handle(self, vinfo):
        for handle_info in self.can_handle_lst:
            if handle_info.tup == vinfo:
                return True
        return False

    def is_mapped_ruyi_index(self, vinfo, index):
        for handle_info in self.can_handle_lst:
            if handle_info.index == index and handle_info.tup == vinfo:
                self.cur_index = index
                return True
        return False

    def handle_version(self, vinfo):
        for handle_info in self.can_handle_lst:
            if handle_info.index == self.cur_index:
                return handle_info.version_mapper(vinfo)
        raise ValueError("No version mapper found")

    def fetch_release(self, vinfo):
        handler = self.find_handler()

        api_url = f"https://api.github.com/repos/{handler.repo}/releases"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-Github-API-Version": "2022-11-28",
        }
        response = self.requests.get(api_url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise ValueError(f"Failed to fetch release info: {response.text}")
        releases = response.json()
        for release in releases:
            if handler.release_filter(vinfo, release):
                return release
        raise ValueError("No release found")

    def extract_download_assest(self, vinfo, gh_release):
        handler = self.find_handler()

        assets = gh_release["assets"]
        for asset in assets:
            if handler.asset_filter(vinfo, asset):
                return asset
        raise ValueError("No download url found in release")

    def handle_report(self, vinfo, index, last_index):
        release = self.fetch_release(vinfo)
        assest = self.extract_download_assest(vinfo, release)

        img_path = self.os.path.join(
            self.__tmppath__, assest["name"]
        )
        img_file = self.download_file(img_path, assest["browser_download_url"])
        img_dist = self.gen_distfile(img_file, assest["browser_download_url"])

        handler = self.find_handler()
        desc = handler.gen_desc(vinfo, index)
        res = self.autoupdate_index(
            last_index[-1], vinfo, desc, {
                "disk": img_dist
            }
        )
        return res


licheervnano_buildroot = HandleInfo(
    "buildroot-sdk-sipeed-licheervnano",
    ("sipeed_licheervnano", "buildroot", "null"),
    lambda vinfo: f"0.{vinfo.version}.0",
    "sipeed/LicheeRV-Nano-Build",
    lambda vinfo, release: vinfo.version in release["name"],
    lambda vinfo, asset: ".img" in asset["name"],
    lambda vinfo, index: f"Buildroot SDK & FreeRTOS image for Sipeed LicheeRV Nano, {
        vinfo.version}"
)

licheervnano_debian = HandleInfo(
    "debian-fishwaldo-sg200x-sipeed-licheervnano",
    ("sipeed_licheervnano", "debian", "null"),
    lambda vinfo: vinfo.version[1:],
    "Fishwaldo/sophgo-sg200x-debian",
    lambda vinfo, release: vinfo.version[1:] in release["name"],
    lambda vinfo, asset: "licheervnano" in asset["name"] and ".img" in asset["name"],
    lambda vinfo, index: "Debian image for Sipeed LicheeRV Nano with Sophgo SG200x, " +
    "from https://github.com/Fishwaldo"
)


mars_buildroot = HandleInfo(
    "debian-desktop-sdk-milkv-mars-sd",
    ("milkv_mars", "buildroot", "null"),
    lambda vinfo: vinfo.version,
    "milkv-mars/mars-buildroot-sdk",
    lambda vinfo, release: vinfo.version in release["name"],
    lambda vinfo, asset: "mars" in asset["name"] and ".img" in asset["name"] and
    "cm" not in asset["name"] and "sd" in asset["name"],
    lambda vinfo, index: f"Official Debian Desktop SDK image for Milk-V Mars v{
        vinfo.version} (SD card)"
)

mars_cm_buildroot = HandleInfo(
    "debian-desktop-sdk-milkv-mars-cm-sd",
    ("milkv_mars", "buildroot", "null"),
    lambda vinfo: vinfo.version,
    "milkv-mars/mars-buildroot-sdk",
    lambda vinfo, release: vinfo.version in release["name"],
    lambda vinfo, asset: "mars" in asset["name"] and ".img" in asset["name"] and
    "cm" in asset["name"] and "sd" in asset["name"],
    lambda vinfo, index: f"Official Debian Desktop SDK image for Milk-V Mars CM v{
        vinfo.version} (SD card)"
)


def register() -> UploadPluginBase | None:
    return GithubReleaseGetter([
        licheervnano_buildroot,
        mars_buildroot,
        mars_cm_buildroot,
        licheervnano_debian
    ])
