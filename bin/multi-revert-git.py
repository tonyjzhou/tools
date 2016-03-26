#!/usr/bin/python

from subprocess import call

files_to_revert = [
    "science/src/java/com/twitter/common_internal/test_security/README",
    "science/src/java/com/twitter/common_internal/test_security/JUnitCheckConnectDecider.java",
    "science/src/java/com/twitter/common_internal/test_security/JUnitSecurityMgr.java",
    "science/tests/java/com/twitter/common_internal/test_security/JUnitCheckConnectDeciderTest.java",
    "science/tests/java/com/twitter/common_internal/test_security/JUnitSecurityMgrTest.java",
]

target_commit = '66a6dd4'

for f in files_to_revert:
    print "Reverting {} to commit {} ...".format(f, target_commit)
    call(["git", "co", target_commit, f])
