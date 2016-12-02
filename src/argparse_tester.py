#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    description='%(prog)s shows and cleans workspaces when garbage greater than a threshold.')
parser.add_argument('--clean', action='store_true', default=False,
                    help="if specified, the workspace will be swept if it's marked (default: %(default)s)")
parser.add_argument('--max_count', type=int, nargs='?', default=15000,
                    help='if count is greater than max_count, the workspace will be marked (default: %(default)s)')
parser.add_argument('--max_packs', type=int, nargs='?', default=15,
                    help='if packs is greater than max_packs, the workspace will be marked (default: %(default)s)')

args = parser.parse_args()
print("clean =", args.clean)
print("max_count =", args.max_count)
print("max_packs =", args.max_packs)
