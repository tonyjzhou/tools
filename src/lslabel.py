#!/usr/bin/python
###############################################################
# Given a list of job names; produce a table of jobs -> labels
###############################################################
import sys


def lslabel(job):
    label = "label"

    # Read /Users/tzhou/workspace/ci-job-configs/.test/output/{job}

    # Extract the label in pattern: <assignedNode>label</assignedNode>

    return (job, label)


def read_file(file_name):
    with open(file_name, 'r') as my_file:
        content = my_file.read()
    return content


def main():
    jobs = sys.argv[1:]
    for job in jobs:
        print lslabel(job)


if __name__ == '__main__':
    main()
