#!/usr/bin/python
###############################################################
# Given a list of job names; produce a table of jobs -> labels
###############################################################
import sys


def lslabel(job):
    label = "label"

    # Read /Users/tzhou/workspace/ci-job-configs/.test/output/{job}

    # Extract the label in xpath: /project/assignedNode

    return (job, label)


def main():
    jobs = sys.argv[1:]
    for job in jobs:
        print lslabel(job)


if __name__ == '__main__':
    main()


def read_file(file_name):
    return None
