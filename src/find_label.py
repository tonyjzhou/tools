#!/usr/bin/env python3
###############################################################
# Given a list of job names; produce a table of jobs -> labels
###############################################################
import os
import re
import sys


def extract_label(job_config):
    p = re.compile("<assignedNode>(.*)</assignedNode>")
    matches = p.search(job_config)
    return matches.group(1) if matches else ""


def read_file(file_name):
    with open(file_name, 'r') as my_file:
        content = my_file.read()
    return content


def read_job_config(job):
    config_dir = "/Users/%s/workspace/ci-job-configs/.test/output/" % os.environ['USER']
    config_file_name = config_dir + job
    job_config = read_file(config_file_name)
    return job_config


def find_label(job):
    job_config = read_job_config(job)
    label = extract_label(job_config)
    return job, label


def main():
    jobs = sys.argv[1:]
    for job in jobs:
        print(find_label(job))


if __name__ == '__main__':
    main()
