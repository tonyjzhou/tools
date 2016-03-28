#!/usr/bin/python

##################################
# Automatically update repository
#
# TODO
# 1. Extract cd into a library
##################################

import os
from os.path import expanduser
from subprocess import PIPE
from subprocess import Popen
from subprocess import call


class cd:
    """Context manager for changing the current working directory"""

    def __init__(self, newPath):
        self.newPath = expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
        print "Entering {} ...\n".format(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
        print "Entering {} ...\n".format(self.savedPath)


def call_with_message(command, message):
    print message

    return_code = call(command)

    if (return_code == 0):
        print message + " done\n"
    else:
        print message + " failed\n"

    return return_code == 0


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

    with cd(dir):
        if (call_with_message(["git", "co", branch],
                              "Switching to branch '{}' ...".format(branch)) and call_with_message(["git", "up"],
                                                                                                   "Pulling and rebasing branch '{}' ...".format(
                                                                                                           branch))):
            print "git update succeeded!\n"


def main():
    current_branch = Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=PIPE).stdout.read().rstrip()
    git_update("~/workspace/source/", 'ee/pants_java8')
    git_update("~/workspace/source/", 'master')
    git_update("~/workspace/source/", current_branch)


if __name__ == '__main__':
    main()
