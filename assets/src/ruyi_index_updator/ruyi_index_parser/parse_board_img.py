"""
Structure of the board index file

See ruyi packages-index definition
"""

import os
import copy
import toml
from awesomeversion import AwesomeVersion


class BoardIndexProvisionable:
    """
    See ruyi packages-index definition
    """
    strategy: str
    partition_map: dict[str] | None

    def __init__(self, d: dict):
        self.strategy = d["strategy"]
        self.partition_map = d.get("partition_map", None)

    def serialize(self) -> dict:
        """
        Serialize
        """
        if self.partition_map is None:
            return {
                "strategy": self.strategy,
            }
        return {
            "strategy": self.strategy,
            "partition_map": self.partition_map,
        }

    def __copy__(self):
        return BoardIndexProvisionable(self.serialize())


class BoardIndexBlob:
    """
    See ruyi packages-index definition
    """
    distfiles: list[str]

    def __init__(self, d: dict):
        self.distfiles = d["distfiles"]

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            "distfiles": self.distfiles,
        }

    def __copy__(self):
        return BoardIndexBlob(self.serialize())


class BoardIndexDistfiles:
    """
    See ruyi packages-index definition
    """
    name: str
    size: int
    urls: list[str]
    checksums: dict[
        "sha256": str,
        "sha512": str,
    ]
    restrict: list[str] | None

    def __init__(self, d: dict):
        self.name = d["name"]
        self.size = d["size"]
        self.urls = d["urls"]
        self.checksums = d["checksums"]
        self.restrict = d.get("restrict", None)

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            "name": self.name,
            "size": self.size,
            "urls": self.urls,
            "checksums": self.checksums,
            "restrict": self.restrict
        }

    def __copy__(self):
        return BoardIndexDistfiles(self.serialize())


class BoardIndexMetadata:
    """
    See ruyi packages-index definition
    """
    desc: str
    vendor: dict[
        "name": str,
        "eula": str,
    ]

    def __init__(self, d: dict):
        self.desc = d["desc"]
        self.vendor = d["vendor"]

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            "desc": self.desc,
            "vendor": self.vendor,
        }

    def __copy__(self):
        return BoardIndexMetadata(self.serialize())


class BoardIndex:
    """
    See ruyi packages-index definition
    """
    format: str
    metadata: BoardIndexMetadata
    distfiles: list[BoardIndexDistfiles]
    blob: BoardIndexBlob
    provisionable: BoardIndexProvisionable

    def __init__(self, d: dict):
        self.format = d["format"]
        self.metadata = BoardIndexMetadata(d["metadata"])
        self.distfiles = [BoardIndexDistfiles(x) for x in d["distfiles"]]
        self.blob = BoardIndexBlob(d["blob"])
        self.provisionable = BoardIndexProvisionable(d["provisionable"])

    def serialize(self) -> dict:
        """
        Serialize
        """
        return {
            "format": self.format,
            "metadata": self.metadata.serialize(),
            "distfiles": [x.serialize() for x in self.distfiles],
            "blob": self.blob.serialize(),
            "provisionable": self.provisionable.serialize(),
        }

    @staticmethod
    def load(path: str) -> "BoardIndex":
        """
        Load from file
        """
        t = toml.load(path)
        return BoardIndex(t)

    def __copy__(self):
        return BoardIndex(self.serialize())


class BoardImages:
    """
    Hold one version of the board image index
    """
    raw_version: str
    is_bot_created: bool
    info: BoardIndex

    @property
    def version(self) -> str:
        """
        return the version
        """
        return self.raw_version

    @version.setter
    def version(self, value: str):
        self.raw_version = value

    def __init__(self, file: str | None = None, *,
                 bot_created: bool = True, version: str = None, info: BoardIndex = None):
        if file is None:
            self.is_bot_created = bot_created
            self.raw_version = version
            self.info = info
            return
        self.is_bot_created = False
        basename = os.path.basename(file)
        self.version = basename[:-5]  # remove .toml
        self.info = BoardIndex.load(file)

    def __copy__(self):
        return BoardImages(bot_created=False,
                           version=copy.copy(self.version), info=copy.copy(self.info)
                           )

    def __cmp__(self, other):
        av1 = AwesomeVersion(self.version)
        if isinstance(other, str):
            av2 = AwesomeVersion(other)
        elif isinstance(other, BoardImages):
            av2 = AwesomeVersion(other.version)
        else:
            raise NotImplementedError
        if av1 > av2:
            return 1
        if av1 < av2:
            return -1
        return 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0
