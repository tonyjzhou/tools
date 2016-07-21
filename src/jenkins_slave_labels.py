#!/usr/bin/env python

import argparse
import json
import urllib

SERVICE_URL = 'https://jinkins-api.twitter.biz/api/1.0/slaves/{}/labels'


def main():
    hosts = [line.rstrip('\n') for line in open('workspace_gc.out')]
    for host in hosts:
        if len(host) < 1: continue
        print "|{}|{}|".format(host, find_labels(host))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='%(prog)s looks for the labels for the slaves.')
    parser.add_argument('--slave_file', type=basestring, nargs='?', default="slaves.txt",
                        help=' (default: %(default)s)')
    return parser.parse_args()


def find_labels(host):
    url = SERVICE_URL.format(host)
    # print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    # print 'Retrieved', len(data), 'characters'
    try:
        js = json.loads(str(data))
    except:
        js = None
    return [v.get('name', 'Unknown').encode("ascii") for v in js]


if __name__ == '__main__':
    main()
