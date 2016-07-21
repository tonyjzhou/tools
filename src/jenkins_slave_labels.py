#!/usr/bin/env python

import json
import urllib

serviceurl = 'https://jinkins-api.twitter.biz/api/1.0/slaves/{}/labels'

hosts = [line.rstrip('\n') for line in open('workspace_gc.out')]

for host in hosts:
    if len(host) < 1: continue

    url = serviceurl.format(host)
    # print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    # print 'Retrieved', len(data), 'characters'

    try:
        js = json.loads(str(data))
    except:
        js = None

    labels = [v.get('name', 'Unknown').encode("ascii") for v in js]

    print "|{}|{}|".format(host, labels)
