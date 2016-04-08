#!/usr/bin/python

##################################
# Automatically update repository
#
# TODO
# * Extract print_banner
##################################

from subprocess import PIPE
from subprocess import Popen

from system.my_os import Cd
from system.my_os import call_with_message


def print_banner(dir, branch):
    message = "git update {} for '{}'".format(dir, branch)
    header = "-" * len(message)

    print header
    print message
    print header
    print


def git_update(dir, branch):
    if not dir or not branch:
        return

    print_banner(dir, branch)

    with Cd(dir):
        if (call_with_message(["git", "co", branch],
                              "Switching to branch '{}' ...".format(branch)) and call_with_message(["git", "up"],
                                                                                                   "Pulling and rebasing branch '{}' ...".format(
                                                                                                       branch))):
            print "git update succeeded!\n"


def main():
    SRC_DIR = "~/workspace/source/"

    with Cd(SRC_DIR):
        current_branch = Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=PIPE).stdout.read().rstrip()

    branches_to_update = ('master', current_branch)
    for branch in branches_to_update:
        git_update(SRC_DIR, branch)


if __name__ == '__main__':
    main()
