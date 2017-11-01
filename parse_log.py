#!/usr/bin/python3

import argparse
import json
import sys

from log_searcher import search, SEARCH_CRITERIA_FUNCTIONS


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parse logs and answer questions.'
    )

    parser.add_argument(
        '--file',
        default='input.json',
        type=argparse.FileType('r'),  # input file must be readable
        help='Log file in JSON that contains all logs, default: input.json',
    )

    parser.add_argument(
        '--criteria',
        required=True,
        choices=list(SEARCH_CRITERIA_FUNCTIONS.keys()),
        help='The search criteria, e.g. maxErrorOperation, longestTransaction'
    )

    args = parser.parse_args()

    try:
        with open(args.file.name, 'r') as f:
            logs = json.load(f)
    except Exception:
        print(f"ERROR: Cannot load JSON data in {args.file.name}")
        sys.exit(1)

    print(search(logs, args.criteria))
    sys.exit(0)
