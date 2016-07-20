#!/usr/bin/python
import os
import re
import subprocess


def main():
    source_dirs = find_all_source_dirs()

    for src_dir in source_dirs:
        os.chdir(src_dir)
        out = capture_git_count_objects_output()
        object_counts = parse_git_count_objects_output(out)
        check_gc_required(object_counts)


def find_all_source_dirs():
    workspace_dir = "/data/jenkins/workspace"
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


def check_gc_required(object_counts):
    count = int(object_counts['count'])
    packs = int(object_counts['packs'])

    if count >= 30000 or packs >= 30:
        print "'git gc' is required for workspace", os.getcwd(), ": count =", count, ", packs =", packs
    else:
        print "'git gc' is NOT required for workspace", os.getcwd()


if __name__ == '__main__':
    main()
