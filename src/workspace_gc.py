#!/usr/bin/python
import argparse
import os
import re
import shutil
import subprocess

workspace_dir = "/data/jenkins/workspace"


def main():
    args = parse_arguments()

    for src_dir in find_all_source_dirs():
        os.chdir(src_dir)
        out = capture_git_count_objects_output()
        object_counts = parse_git_count_objects_output(out)
        if check_gc_required(object_counts, args.max_count, args.max_packs) and args.clean:
            clean_workspace(src_dir)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='%(prog)s shows and cleans workspaces when garbage greater than a threshold.')
    parser.add_argument('--clean', action='store_true', default=False,
                        help="if specified, the workspace will be swept if it's marked (default: %(default)s)")
    parser.add_argument('--max_count', type=int, nargs='?', default=15000,
                        help='if count is greater than max_count, the workspace will be marked (default: %(default)s)')
    parser.add_argument('--max_packs', type=int, nargs='?', default=15,
                        help='if packs is greater than max_packs, the workspace will be marked (default: %(default)s)')
    return parser.parse_args()


def clean_workspace(src_dir):
    print 'Cleaning', src_dir, "..."

    print 'cd', workspace_dir
    os.chdir(workspace_dir)

    print 'rmtree', src_dir, "..."
    shutil.rmtree(src_dir, ignore_errors=True)
    print 'rmtree', src_dir, "... done"

    print 'git', 'clone', '--single-branch', '-b', 'master', '--verbose', '--reference', '/data/jenkins/git/source.git', 'https://git.twitter.biz/ro/source', src_dir
    p = subprocess.Popen(
        ['git', 'clone', '--single-branch', '-b', 'master', '--verbose', '--reference', '/data/jenkins/git/source.git',
         'https://git.twitter.biz/ro/source', src_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print out

    print 'Cleaning', src_dir, "... done"
    return out


def find_all_source_dirs():
    source_dirs = sorted([os.path.join(workspace_dir, name) for name in os.listdir(workspace_dir) if
                          (name.startswith("source") and os.path.isdir(os.path.join(workspace_dir, name)))])
    # print source_dirs
    return source_dirs


def capture_git_count_objects_output():
    p = subprocess.Popen(['git', 'count-objects', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    # print out
    return out


def parse_git_count_objects_output(out):
    regex = re.compile(r"\b(\w+)\s*:\s*([^:]*)(?=\s+\w+\s*:|$)")
    object_counts = dict(regex.findall(" ".join(out.replace('-', '').split())))
    # print object_counts
    return object_counts


def check_gc_required(object_counts, max_count, max_packs):
    count = int(object_counts.get('count', 0))
    packs = int(object_counts.get('packs', 0))

    if count >= max_count or packs >= max_packs:
        print "'git gc' is required for workspace", os.getcwd(), ": count =", count, ", packs =", packs
        return True
    else:
        print "'git gc' is NOT required for workspace", os.getcwd(), ": count =", count, ", packs =", packs
        return False


if __name__ == '__main__':
    main()
