#!/usr/bin/env python3
"""
Automatically check the index of ruyi and renew it.
"""

import os
import shutil
import argparse
import tempfile
import logging
import colorlog

from src.matrix_parser import Systems, ImageStatus
from src.ruyi_index_updator import RuyiDiff, RuyiGitRepo


def main():
    """
    Main function
    """

    arg = argparse.ArgumentParser()
    arg.add_argument('-c', '--config', help='config file',
                     default='assets/config.toml')
    arg.add_argument(
        '-p', '--path', help='path to the support matrix', default='.')
    arg.add_argument(
        '-i', '--index', help='path clone of ruyi index, default to a temp dir', default=None
    )
    arg.add_argument(
        '--pr', help='create a PR for the update', action='store_true'
    )
    arg.add_argument(
        '--log', help='output the log to the file', default=None
    )
    arg.add_argument(
        '--warn', help='output the warn to the file', default=None
    )
    arg.add_argument(
        '--threadhold', help='the status threadhold can be synced', default='basic'
    )
    arg.add_argument(
        '--force', help='force to update the index', action='store_true'
    )
    arg.add_argument(
        'plugin_names', help='the plugins to run, default to all', nargs='*'
    )
    args = arg.parse_args()

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s[%(relativeCreated)d %(levelname)s]%(reset)s: %(message)s'))

    handlers = [handler]

    if args.log is not None:
        p = os.path.abspath(args.log)
        log_handler = logging.FileHandler(p)
        log_handler.setFormatter(logging.Formatter(
            '%(relativeCreated)d %(levelname)s: %(message)s'))
        log_handler.setLevel(logging.INFO)
        handlers.append(log_handler)

    if args.warn is not None:
        p = os.path.abspath(args.warn)
        warn_handler = logging.FileHandler(p)
        warn_handler.setFormatter(logging.Formatter(
            '%(relativeCreated)d %(levelname)s: %(message)s'))
        warn_handler.setLevel(logging.WARNING)
        handlers.append(warn_handler)

    logging.basicConfig(level=logging.INFO, handlers=handlers)

    logger = logging.getLogger()

    index_path = args.index
    if index_path is None:
        index_path = tempfile.mkdtemp()

    matrix = Systems(args.path)
    diffs = RuyiDiff(matrix, args.config)
    repo = RuyiGitRepo(index_path)
    force = args.force if args.force else False

    threadhold = ImageStatus(args.threadhold)
    for diff in diffs.gen_diff(args.plugin_names, threadhold, force):
        pr = repo.upload_image(diff)
        if pr is None:
            continue
        if not args.pr:
            logger.info("%s", repr(pr))
            continue
        if force:
            pr.title = f"[Force Update] {pr.title}"
        repo.create_wrapped_pr(pr, force)

    if args.index is None:
        shutil.rmtree(index_path)


if __name__ == '__main__':
    main()
