#!/usr/bin/env python3

from __future__ import print_function

import argparse
import json
import os
import urllib

SERVICE_URL = 'https://jinkins-api.twitter.biz/api/1.0/masters/{}/slaves'


def main():
    args = parse_arguments()

    hosts = [line.rstrip('\n') for line in open(args.masters_file)]
    for host in hosts:
        if len(host) < 1: continue

        slaves = "\n".join([slave for slave in find_slaves(host) if 'office' not in slave])

        print_to_console(host, slaves)
        print_to_file(host, slaves)


def print_to_console(host, slaves):
    print(host)
    print(slaves, "\n")


def print_to_file(host, slaves):
    sub_dir = 'slaves'
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)

    filename = "slaves_{}.txt".format(host.split('.')[0])
    with open(os.path.join(sub_dir, filename), 'w') as f:
        print(slaves, file=f)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='%(prog)s looks for all the slaves for the master.')
    parser.add_argument('--masters_file', type=str, nargs='?', default="masters.in",
                        help=' (default: %(default)s)')
    return parser.parse_args()


def find_slaves(host):
    url = SERVICE_URL.format(host)
    uh = urllib.urlopen(url)
    data = uh.read()

    try:
        js = json.loads(str(data))
    except:
        js = None

    # print js
    return [v.get('hostname', 'Unknown').encode("ascii") for v in js]


if __name__ == '__main__':
    main()
