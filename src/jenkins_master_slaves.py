#!/usr/bin/env python

import argparse
import json
import urllib

SERVICE_URL = 'https://jinkins-api.twitter.biz/api/1.0/masters/{}/slaves'


def main():
    args = parse_arguments()

    hosts = [line.rstrip('\n') for line in open(args.masters_file)]
    for host in hosts:
        if len(host) < 1: continue
        print host
        print "\n".join(find_slaves(host)), "\n"


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
