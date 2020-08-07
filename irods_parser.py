#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-08-07
Purpose: Parse iRODS "ils" output
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Parse iRODS "ils" output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=sys.stdin,
                        nargs='?')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dir_re = re.compile(r'^(\/[^:]+)')
    coll_re = re.compile(r'^\s{2}C-\s+')
    file_re = re.compile(r'^\s{2}([^/]+)')

    cur_dir = ''
    for line in map(str.rstrip, args.input):
        dir_match = dir_re.search(line)
        coll_match = coll_re.search(line)
        file_match = file_re.search(line)

        if dir_match:
            cur_dir = dir_match.group(1)
        elif coll_match:
            continue
        elif file_match and cur_dir:
            filename = file_match.group(1)
            print(os.path.join(cur_dir, filename))


# --------------------------------------------------
if __name__ == '__main__':
    main()
