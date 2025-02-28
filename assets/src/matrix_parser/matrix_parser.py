"""
Parse metadata of systems and boards
"""
import os
from typing import Any
from functools import total_ordering
import yaml
import frontmatter

LANG = [
    'zh'
]

@total_ordering
class ImageStatus:

    MAPPER = {
        'wip': ('WIP', 1),
        'cfh': ('CFH', 2),
        'cft': ('CFT', 3),
        'basic': ('Basic', 4),
        'good': ('Good', 5),
    }

    def __init__(self, status: str):
        self.status = status.lower()

    def __str__(self):
        return self.MAPPER[self.status][0]
    
    def __len__(self):
        return len(self.MAPPER[self.status][0])
    
    def __repr__(self):
        return self.MAPPER[self.status][0]
    
    def __eq__(self, other):
        return self.MAPPER[self.status][1] == self.MAPPER[other.status][1]
    
    def __lt__(self, other):
        return self.MAPPER[self.status][1] < self.MAPPER[other.status][1]

class SystemVar:
    """
    This is for a system varient, like normal Ubuntu/ Ubuntu LTS / Ubuntu with desktop and so on.
    eg:
    ---
    sys: deepin
    sys_ver: 23
    sys_var: null

    status: basic
    last_update: 2024-06-21
    ---
    """
    sys: str
    sys_ver: str | None
    sys_var: str | None
    status: ImageStatus
    last_update: str
    link: list[str] | None

    raw_data: Any  # Store the raw data of the readed metadata

    def __init_by_file(self, meta_path, link: list[str]):
        self.link = link
        if not os.path.exists(meta_path):
            raise FileNotFoundError(f"{meta_path} not found")
        with open(meta_path, 'r', encoding="utf-8") as file:
            try:
                post = frontmatter.load(file)
            except Exception as _:
                raise FileNotFoundError(
                    f"{meta_path} has no frontmatter") from _
            if 'sys' not in post.keys():
                raise FileNotFoundError(f"{meta_path} has no frontmatter")
            self.raw_data = post
            if post['sys'] == 'revyos':
                self.sys = 'debian'
            else:
                self.sys = post['sys']
            self.sys_ver = post['sys_ver']
            self.sys_var = post['sys_var']
            self.status = ImageStatus(post['status'])
            self.last_update = post['last_update']

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.sys = kwargs['sys'].lower()
            self.sys_ver = kwargs['sys_ver']
            self.sys_var = kwargs['sys_var']
            self.status = ImageStatus(kwargs['status'])
            self.last_update = kwargs['last_update']
            self.link = kwargs['link']
        else:
            self.__init_by_file(*args, **kwargs)


class System:
    """
    This is for a type of system, like Ubuntu
    """
    sys: str
    variant: list[SystemVar]

    def __len__(self):
        return len(self.variant)

    def is_md(self, s: str):
        """
        If a file name be like `xxx.md`, then it should be markdown file
        """
        return s.endswith('.md')

    def is_tranlate(self, s: str):
        """
        If a file name be like `xxx_lang.md`, then it should be translated
        """
        if 'blink' in s:
            # Temporary fix for blink.md,
            # this file is not a system-board test, need migrate to other place
            return True
        for lang in LANG:
            if f'_{lang}.md' in s:
                return True
        return False

    def __init_by_folder(self, folder: str, base_link=""):
        # walk through every file in the folder
        check_success = True
        self.variant = []
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, file)):
                continue
            if not self.is_md(file):
                continue
            if self.is_tranlate(file):
                continue
            try:
                path = os.path.join(folder, file)
                link = [base_link, os.path.basename(folder), file]
                system_var = SystemVar(path, link)
                self.variant.append(system_var)
            except FileNotFoundError as e:
                check_success = False
                print(f"Error: {e}")
                continue
        if not check_success:
            raise FileNotFoundError(
                f"Some metadata not found for system: {os.path.basename(folder)}")

    def __init__(self, *args, **kwargs):
        self.variant = []
        if len(kwargs) > 0:
            var = SystemVar(*args, **kwargs)
            self.variant.append(var)
        else:
            self.__init_by_folder(*args, **kwargs)
        if len(self.variant) == 0:
            raise FileNotFoundError("No metadata found")
        self.sys = self.variant[0].sys


class Board:
    """
    a collection of systems and eg:
    ---
    product: VisionFive 2
    cpu: JH7110
    cpu_core: SiFive U74 + SiFive S7 + SiFive E24
    ---
    """
    vendor: str | None
    product: str
    cpu: str
    link: str
    cpu_core: str
    systems: list[System]

    raw_data: Any  # Store the raw data of the readed metadata

    def append_system(self, system: System):
        """
        append a system to the board
        """
        self.systems.append(system)

    def gen_row(self, system_arr: dict[str]):
        """
        generate a row of the table
        """
        row = [
            self.cpu,
            self.cpu_core,
            self.link,
            self
        ]

        na_count = 0

        for k, _ in system_arr.items():
            for system in self.systems:
                if system.sys == k:
                    row.append(system)
                    break
            else:
                row.append('N/A')
                na_count += 1

        if na_count == len(system_arr):
            return None

        return row

    def strip(self):
        """
        dummy for strip the board
        """
        self.product = self.product.strip()
        return self

    def __str__(self):
        return self.product

    def __len__(self):
        return len(self.product)

    def __init__(self, path: str):
        check_success = True
        base_name = os.path.basename(path)
        self.link = base_name
        readme_path = os.path.join(path, 'README.md')
        if not os.path.exists(readme_path):
            raise FileNotFoundError(f"{readme_path} not found")
        with open(readme_path, 'r', encoding="utf-8") as file:
            post = frontmatter.load(file)
            self.raw_data = post
            self.vendor = post.get('vendor', None)
            self.product = post['product']
            self.cpu = post['cpu']
            self.cpu_core = post['cpu_core']
        self.systems = []

        for folder in os.listdir(path):
            f = os.path.join(path, folder)
            if os.path.isdir(f):
                try:
                    system = System(f, self.link)
                except FileNotFoundError as e:
                    check_success = False
                    print(f"Error: {e}")
                    continue
                self.append_system(system)

        if not os.path.exists(os.path.join(path, 'others.yml')):
            return
        with open(os.path.join(path, 'others.yml'), 'r', encoding="utf-8") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            for i in data:
                system = System(
                    sys=i['sys'],
                    sys_ver=i['sys_ver'],
                    sys_var=i['sys_var'],
                    status=i['status'],
                    last_update='2000-00-00',
                    link=[self.link, 'others.yml']
                )
                self.append_system(system)
        if not check_success:
            raise FileNotFoundError(
                f"Some metadata not found for board: {self.product}")


class Systems:
    """
    support matrix of systems
    """
    linux: dict[str]
    bsd: dict[str]
    rtos: dict[str]
    others: dict[str]
    customized: dict[str]

    exclude_dir = [
        '.github',
        'assets',
        '.git',
        '.vscode',
        '__pycache__',
        '~', # ?
    ]

    def should_exclude(self, path):
        """
        check if the path should be excluded
        """
        for name in self.exclude_dir:
            if name in path:
                return True
        if path[0] == '.':
            return True
        return False
    boards: list[Board]

    def __init__(self, path):
        check_success = True
        meta_path = os.path.join(path, 'assets', 'metadata.yml')
        with open(meta_path, 'r', encoding="utf-8") as file:
            def mp(x):
                res = {}
                for l in x:
                    for i in l.items():
                        res[i[0]] = i[1]
                return res
            data = yaml.load(file, Loader=yaml.FullLoader)
            self.linux = mp(data['linux'])
            self.bsd = mp(data['bsd'])
            self.rtos = mp(data['rtos'])
            self.others = mp(data['others'])
            self.customized = mp(data['customized'])
        self.boards = []
        for folder in os.listdir(path):
            if self.should_exclude(folder):
                continue
            p = os.path.join(path, folder)
            if not os.path.isdir(p):
                continue
            try:
                board = Board(p)
                self.boards.append(board)
            except FileNotFoundError as e:
                check_success = False
                print(f"Error: {e}")
                continue
        if not check_success:
            raise FileNotFoundError("Some metadata not found")
        # Sort boards by product name
        self.boards.sort(key=lambda x: x.product)
