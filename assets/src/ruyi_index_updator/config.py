"""
Store the config for the ruyi index updator
"""

import os
import argparse
from typing import TypedDict, ReadOnly, NotRequired


class CFG():
    """
    Wrapper for the args to act as a singleton dict
    """

    class CFGOne(TypedDict):
        """
        The type of the cli config
        """
        name: ReadOnly[str]
        short_name: NotRequired[ReadOnly[str]]
        explain: NotRequired[ReadOnly[str]]
        default: NotRequired[ReadOnly[str]]
        action: NotRequired[ReadOnly[str]]
        nargs: NotRequired[ReadOnly[str]]

    def __set_arg(self, arg: argparse.ArgumentParser, c: CFGOne):
        if "short_name" in c:
            arg.add_argument(
                f'-{c["short_name"]}',
                f'--{c["name"]}',
                help=c["explain"] if "explain" in c else None,
                default=c["default"] if "default" in c else None,
                action=c["action"] if "action" in c else None,
            )
        else:
            arg.add_argument(
                f'--{c["name"]}',
                help=c["explain"] if "explain" in c else None,
                default=c["default"] if "default" in c else None,
                action=c["action"] if "action" in c else None,
            )

    def __init__(self, config_list: list[CFGOne]):
        arg = argparse.ArgumentParser()
        for c in config_list:
            self.__set_arg(arg, c)
        args = arg.parse_args()
        self.configs = args

    def __getitem__(self, key: str):
        return self.configs.__getattribute__(key)


_cli_configs = CFG([
    {'name': 'config', 'short_name': 'c',
        'explain': 'path to config file', 'default': 'assets/config.toml'},
    {'name': 'path', 'short_name': 'p',
        'explain': 'path to the support matrix', 'default': '.'},
    {'name': 'index', 'short_name': 'i',
        'explain': 'path to clone ruyi index, default to a temp dir'},
    {'name': 'pr', 'explain': 'should create a PR for the update', 'action': 'store_true'},
    {'name': 'log', 'explain': 'output the log to the file', 'default': None},
    {'name': 'warn', 'explain': 'output the warn to the file', 'default': None},
    {'name': 'threadhold', 'explain': 'the status threadhold can be synced',
        'default': 'basic'},
    {'name': 'force', 'explain': 'force to update the index', 'action': 'store_true'},
    {'name': 'plugin_names', 'explain': 'the plugins to run, default to all', 'nargs': '*'}
])

_internal_configs = {
    "RUYI_PACKAGE_INDEX": "git@github.com:ruyisdk/packages-index.git",
    "CACHE_DIR": os.environ.get("CACHE_DIR", None)
}


class CFGdict():
    """
    Dict like wrapper for the config, merge the cli config and internal config
    """

    __d = {}

    def __getitem__(self, key: str):
        if key in self.__d:
            return self.__d[key]
        elif key in _cli_configs.configs:
            return _cli_configs[key]
        elif key in _internal_configs:
            return _internal_configs[key]
        else:
            return None

    def __setitem__(self, key: str, value):
        self.__d[key] = value


config = CFGdict()
