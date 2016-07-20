#!/usr/bin/python
import os
import subprocess


def main():
    # find all the source_* directories
    workspace_dir = "/data/jenkins/workspace"
    source_dirs = sorted([os.path.join(workspace_dir, name) for name in os.listdir(workspace_dir) if
                          (name.startswith("source") and os.path.isdir(os.path.join(workspace_dir, name)))])

    print source_dirs

    # cd to each of the source_* directory
    for dir in source_dirs:
        os.chdir(dir)
        print os.getcwd()

        # capture the output of "git count-objects -v"
        p = subprocess.Popen(['git', 'count-objects', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print out

        # parse output

        # for outputs with "count >= 30000" and "packs>=30"
        #   do "git gc"

        # call(["git", "co", target_commit, my_file])


if __name__ == '__main__':
    main()
