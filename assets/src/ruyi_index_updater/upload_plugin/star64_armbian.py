# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring

from .prelude import *

__version__ = "0.0.1"

class Star64Armbian(UploadPluginBase):

    @staticmethod
    def get_name() -> str:
        return "star64_armbian"

    can_handle_tup = {
        "armbian-pine64-star64": ("pine64_star64", "armbian", "null"),
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
        return vinfo.version

    def handle_report(self, vinfo, index, last_index):
        url = vinfo.raw_data.raw_data["link"]
        if url is None or not isinstance(url, str) or len(url) == 0:
            raise ValueError("No link found in version info")

        file_name = url.split("/")[-1]

        img_path = self.os.path.join(
            self.__tmppath__, file_name
        )
        img_file = self.download_file(img_path, url)
        img_dist = self.gen_distfile(img_file, url)

        desc = f"Armbian {vinfo.version} image for Pine64 Star64"
        res = self.autoupdate_index(
            last_index[-1], vinfo, desc, {
                "disk": img_dist
            }
        )
        return res


def register() -> UploadPluginBase | None:
    return Star64Armbian()
