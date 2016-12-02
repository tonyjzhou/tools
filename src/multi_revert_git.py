#!/usr/bin/env python3

from subprocess import call


def multi_revert_git(files_to_revert, target_commit):
    for my_file in files_to_revert:
        print("Reverting {} to commit {} ...".format(my_file, target_commit))
        call(["git", "co", target_commit, my_file])


def main():
    files_to_revert = [
        "science/src/java/com/twitter/common_internal/test_security/README",
        "science/src/java/com/twitter/common_internal/test_security/JUnitCheckConnectDecider.java",
        "science/src/java/com/twitter/common_internal/test_security/JUnitSecurityMgr.java",
        "science/tests/java/com/twitter/common_internal/test_security/JUnitCheckConnectDeciderTest.java",
        "science/tests/java/com/twitter/common_internal/test_security/JUnitSecurityMgrTest.java",
    ]
    target_commit = '66a6dd4'

    multi_revert_git(files_to_revert, target_commit)


if __name__ == '__main__':
    main()
