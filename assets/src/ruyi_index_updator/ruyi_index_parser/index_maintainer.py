"""
Retrieve the ruyi package index from github, and store it in a temporary directory.
"""
import os
import git

from .. import util
from ..config import config
from .parse_board_img import BoardImages

def clone_package_index(path: str):
    """
    Clone the ruyi package index to the path.
    """
    repo = git.Repo.clone_from(config["RUYI_PACKAGE_INDEX"], path)
    return repo

class PackageIndex():
    """
    Resource holder for the ruyi package index.

    Aquire the ruyi package index from github, and store it in a temporary directory.
    """

    def __init__(self):
        self.repo = None
        self.tempdir = None

        self.tempdir = util.folder_tmp_mux(None)
        self.__clone(self.tempdir, config["RUYI_PACKAGE_INDEX"])

    def __clone(self, path, url):
        self.repo = git.Repo.clone_from(url, path)

    def _get_path(self) -> str:
        return self.tempdir

    def __enter__(self):
        return PackageIndexProc(self.tempdir)

    def __exit__(self, exc_type, exc_value, traceback):
        self.repo.close()
        self.repo = None

class PackageIndexProc():
    """
    Processor for the ruyi package index.
    """

    def __init__(self, path: str):
        self.path = path

    def parse_board(self) -> dict[str, list[BoardImages]]:
        """
        Parse the board-image manifest file.
        """
        res: dict[str, list[BoardImages]] = {}
        b_path = os.path.join(self.path, "manifests", "board-image")
        for d in os.listdir(b_path):
            d_f = os.path.join(b_path, d)
            if not os.path.isdir(d_f):
                continue
            images = os.listdir(d_f)
            res[d] = [BoardImages(os.path.join(d_f, x)) for x in images]
            res[d].sort()
        return res
