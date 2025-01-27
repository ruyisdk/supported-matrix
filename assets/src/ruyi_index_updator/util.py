"""
Utils
"""

import atexit
import tempfile
import shutil


def folder_tmp_mux(folder: str | None) -> str:
    """
    If the folder is None, return a tmp folder.

    Clean the tmp folder if created.

    A special usage is to use it as a automatiaclly clean tmp folder **after** the program ends,
    as tmpfile only gives this ability in the context manager.
    """
    p = folder if folder is not None else tempfile.mkdtemp()

    def __release_tmp_path():
        shutil.rmtree(p)
    if folder is None:
        atexit.register(__release_tmp_path)
    return p
