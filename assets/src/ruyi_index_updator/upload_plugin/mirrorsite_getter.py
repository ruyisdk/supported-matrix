# pylint: disable=import-outside-toplevel, missing-function-docstring, missing-module-docstring, wildcard-import, unused-wildcard-import, missing-class-docstring
"""
Handle most common image comes from a mirror site
"""

from typing import TypedDict, Required, Protocol

from .prelude import *

__version__ = "0.0.1"


class Info(TypedDict):

    index_name: str
    tup: tuple[str, str, str]

    class VersionMapper(Protocol):
        def __call__(self, vinfo: VInfo) -> str: ...
    version_mapper: Required[VersionMapper]

    # Ideally, path of an image should be like:
    # f"{mirrorsite_url}/{split_path}/{version}/{file}"
    # For example:
    #   https://mirror.iscas.ac.cn/
    #       revyos/extra/images/lpi4a/
    #           20250123/
    #               root-lpi4a-20250123_195216.ext4.zst
    # But... Some image simply doesn't want to follow this format.
    # A fallback is needed.
    class URLInfo(TypedDict):
        mirrorsite_url: Required[str]
        split_path: Required[str]

    class URLGenerator(Protocol):
        def __call__(self, vinfo: VInfo) -> str: ...
    url: Required[URLInfo | URLGenerator]

    class FileNameFilter(Protocol):
        def __call__(self, vinfo: VInfo, file_name: str) -> bool: ...
    file_name_filter: Required[FileNameFilter]

    class GenDesc(Protocol):
        def __call__(self, vinfo: VInfo, index_name: str) -> str: ...
    gen_desc: Required[GenDesc]


class MirrorsiteGetter(UploadPluginBase):

    import urllib
    import bs4

    @staticmethod
    def get_name() -> str:
        return "mirrorsite_getter"

    handler_lst: list[Info]

    # In handel version, we need to know which index we are handling.
    # In design, a single plugin should handle only one index.
    # So we need to pass the index to the function.
    cur_index: str

    def __find_handler_tup(self, vinfo: VInfo) -> Info | None:
        for handler in self.handler_lst:
            if handler["tup"] == vinfo:
                return handler
        return None

    def __find_handler_idx(self, index: str | None = None) -> Info | None:
        if index is None:
            index = self.cur_index
        for handler in self.handler_lst:
            if handler["index_name"] == index:
                return handler
        return None

    def can_handle(self, vinfo: VInfo):
        return self.__find_handler_tup(vinfo) is not None

    def all_index_can_handle(self):
        res = {
            i["index_name"]: i["tup"] for i in self.handler_lst
        }
        return res

    def is_mapped_ruyi_index(self, vinfo: VInfo, index: str):
        self.cur_index = index
        handler = self.__find_handler_tup(vinfo)
        if handler is None:
            raise RuntimeError(
                f"No handler found for {index} in mirrorsite getter")
        return handler["index_name"] == index

    def handle_version(self, vinfo: VInfo):
        handler = self.__find_handler_tup(vinfo)
        if handler is None:
            raise RuntimeError(
                f"No handler found for {vinfo} in mirrorsite getter")
        return handler["version_mapper"](vinfo)

    def handle_report(self, vinfo: VInfo,
                      index: str, last_index: list[BoardImages]) -> BoardImages:
        handler = self.__find_handler_idx()
        if handler is None:
            raise RuntimeError(
                f"No handler found for {self.cur_index} in mirrorsite getter")

        if callable(handler["url"]):
            page_url = handler["url"](vinfo)
        else:
            image_url = self.urljoin(
                handler["url"]["mirrorsite_url"],
                handler["url"]["split_path"],
            )
            page_url = self.urljoin(
                image_url,
                vinfo.version
            )

        html = self.requests.get(page_url, timeout=90).text

        soup = self.bs4.BeautifulSoup(html, "html5lib")

        hyperlinks = soup.select('a')

        file_link = None
        file_path = None
        for link in hyperlinks:
            if not link.has_attr("href"):
                continue
            if handler["file_name_filter"](vinfo, str(link["href"])):
                file_link = self.urljoin(
                    page_url, str(link["href"]))
                file_name = self.urlbasename(file_link)
                file_path = self.os.path.join(
                    self.__tmppath__, file_name)

        if file_link is None:
            self.logger.error(
                "Failed to filter a name in index %s", self.cur_index)
            raise RuntimeError(
                f"Failed to filter a name in index {self.cur_index}")

        file = self.download_file(file_path, file_link)
        dist = self.gen_distfile(file, file_link)

        desc = handler["gen_desc"](vinfo, self.cur_index)

        res = self.autoupdate_index(
            last_index[-1], vinfo, desc, {
                "disk": dist
            }
        )
        return res

    def __init__(self, _handler_lst: list[Info]):
        super().__init__()
        self.handler_lst = _handler_lst
        self.cur_index = ""


bpif3_bianbu: Info = {
    "index_name": "bianbu-bpi-f3",
    "tup": ("bpi_f3", "bianbu", "null"),
    "version_mapper": lambda vinfo: vinfo.version[1:],
    "url": {
        "mirrorsite_url": "https://archive.spacemit.com/",
        "split_path": "image/k1/version/bianbu/"
    },
    "file_name_filter": lambda vinfo, filename:
        "desktop" in filename and
        "k1" in filename and
        "img" in filename and
        "md5" not in filename,
    "gen_desc": lambda vinfo, index_name:
        f"Official bianbu desktop image for Banana Pi F3 version {
            vinfo.version}",
}

pioneer_revyos: Info = {
    "index_name": "revyos-sg2042-milkv-pioneer",
    "tup": ("milkv_pioneer", "debian", "null"),
    "version_mapper": lambda vinfo: f"0.{vinfo.version}.0",
    "url": {
        "mirrorsite_url": "https://mirror.iscas.ac.cn/",
        "split_path": "revyos/extra/images/sg2042/"
    },
    "file_name_filter": lambda vinfo, filename:
    "revyos" in filename and
        "pioneer" in filename and
        "img" in filename,
    "gen_desc": lambda vinfo, index_name:
        f"RevyOS {vinfo.version} image for Milk-V Pioneer Box with SG2042"
}


def openkylin_mapper(vinfo: VInfo) -> str:
    """
    openKylin doesn't totally follow the versioning rule.
    Seen 2.0 as 2.0.0-0 and 2.0-sp1 as 2.0.0-1, 
    so if some day they really release something like 2.0.1-rc-sp1, then it still works fine.
    """
    m = re.match(
        r"(\d+)\.(\d+)(\.(\d+))?((-(?:(?!SP)\w+))*)(-SP(\d+))?((-(\w+))*)?((\+(\w+))*)?",
        vinfo.version)
    return f"{m[1]}.{m[2]}.{m[4] or 0}-{m[8] or 0}{m[5]}{m[9]}{m[12]}"


bpif3_openkylin: Info = {
    "index_name": "openkylin-bpi-f3",
    "tup": ("bpi_f3", "openkylin", "null"),
    "version_mapper": openkylin_mapper,
    "url": {
        "mirrorsite_url": "https://mirrors.hust.edu.cn/",
        "split_path": "openkylin-cdimage/"
    },
    "file_name_filter": lambda vinfo, filename:
        "openKylin-Embedded" in filename and
        "spacemit-k1" in filename,
    "gen_desc": lambda vinfo, index_name:
        f"Official OpenKylin Embedded image for Banana Pi F3 version {
            vinfo.version}",
}

pioneer_openkylin: Info = {
    "index_name": "openkylin-sg2042-milkv-pioneer",
    "tup": ("milkv_pioneer", "openkylin", "null"),
    "version_mapper": openkylin_mapper,
    "url": {
        "mirrorsite_url": "https://mirrors.hust.edu.cn/",
        "split_path": "openkylin-cdimage/"
    },
    "file_name_filter": lambda vinfo, filename:
    "openKylin-Embedded" in filename and
        "milk-v-pioneer" in filename,
    "gen_desc": lambda vinfo, index_name:
        f"Official OpenKylin Embedded image for Milk-V Pioneer Box with SG2042 version {vinfo.version}",
}


def register() -> UploadPluginBase | None:
    return MirrorsiteGetter([
        bpif3_bianbu,
        bpif3_openkylin,
        pioneer_revyos,
        pioneer_openkylin
    ])
