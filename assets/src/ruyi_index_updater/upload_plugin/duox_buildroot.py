# pylint: disable=import-outside-toplevel, missing-function-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
"""
Upload plugin for Milk-V Duo family buildroot
"""

from .prelude import *

__version__ = "0.0.1"


class DuoxBuildRoot(UploadPluginBase):

    @staticmethod
    def get_name() -> str:
        return "duox_buildroot"

    can_handle_tup = {
        "buildroot-sdk-milkv-duo": ("milkv_duo", "buildroot", "null"),
        "buildroot-sdk-milkv-duo256m": ("milkv_duo256m", "buildroot", "null"),
        "buildroot-sdk-milkv-duos-sd": ("milkv_duos", "buildroot", "null"),
    }

    def can_handle(self, vinfo: VInfo) -> bool:
        if vinfo in self.can_handle_tup.values():
            return True
        return False

    def is_mapped_ruyi_index(self, vinfo: VInfo, index: str) -> bool:
        if index in self.can_handle_tup and self.can_handle_tup[index] == vinfo:
            return True
        return False

    def handle_version(self, vinfo: VInfo) -> str:
        return vinfo.version[1:]

    def fetch_release(self, vinfo: VInfo) -> dict:
        api_url = 'https://api.github.com/repos/milkv-duo/duo-buildroot-sdk/releases'
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-Github-API-Version": "2022-11-28",
        }
        response = self.requests.get(api_url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise ValueError(f"Failed to fetch release info: {response.text}")

        releases = response.json()
        for release in releases:
            if release["name"] == vinfo.version:
                return release
        raise ValueError("No release found")

    def extract_download_assest(self, vinfo: VInfo, gh_release: dict) -> dict:
        assets = gh_release["assets"]
        for asset in assets:
            if asset["name"].startswith(f"milkv-{vinfo.vendor[6:]}-") \
                    and "sd" in asset["name"]:
                return asset
        raise ValueError("No download url found in release")

    def handle_report(self, vinfo: VInfo,
                      index: str, last_index: list[BoardImages]) -> BoardImages:

        if not self.is_mapped_ruyi_index(vinfo, index):
            raise ValueError("Invalid index for this plugin")

        release = self.fetch_release(vinfo)
        assest = self.extract_download_assest(vinfo, release)

        img_path = self.os.path.join(
            self.__tmppath__, assest["name"]
        )
        img_file = self.download_file(img_path, assest["browser_download_url"])
        img_dist = self.gen_distfile(img_file, assest["browser_download_url"])

        desc = f"Official Buildroot SDK image for Milk-V Duo (64M RAM) {assest['name']}"
        res = self.autoupdate_index(
            last_index[-1], vinfo, desc, {
                "disk": img_dist
            }
        )
        return res


def register() -> UploadPluginBase | None:
    return DuoxBuildRoot()
