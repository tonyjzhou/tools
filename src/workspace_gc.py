#!/usr/bin/python
import os


# from subprocess import call


def main():
    # find all the source_* directories
    workspace_dir = "/data/jenkins/workspace"
    source_dirs = sorted([name for name in os.listdir(workspace_dir) if
                          (name.startswith("source") and os.path.isdir(os.path.join(workspace_dir, name)))])

    print source_dirs

    # cd to each of the source_* directory

    # capture the output of "git count-objects -v"

    # for outputs with "count >= 30000" and "packs>=30"
    #   do "git gc"

    # call(["git", "co", target_commit, my_file])


if __name__ == '__main__':
    main()
