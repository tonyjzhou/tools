#!/usr/bin/python

from multiprocessing import Pool
from subprocess import check_output


def sftp(hostname):
    return check_output(["sftp", "-b", "sftp.batch", "tzhou@{}".format(hostname)])


def main():
    pool = Pool()

    results = [pool.apply_async(sftp, ["atla-age-03-sr1.prod.twttr.net"]),
               pool.apply_async(sftp, ["atla-ajz-29-sr3.prod.twttr.net"]),
               pool.apply_async(sftp, ["atla-akk-03-sr2.prod.twttr.net"]),
               pool.apply_async(sftp, ["atla-ate-11-sr1.prod.twttr.net"]),
               pool.apply_async(sftp, ["atla-bmv-19-sr2.prod.twttr.net"]),
               pool.apply_async(sftp, ["smf1-auc-19-sr4.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-aun-19-sr2.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-avp-37-sr3.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-bxb-29-sr3.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-bxg-22-sr4.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-ees-20-sr1.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-eev-08-sr1.prod.twitter.com"]),
               pool.apply_async(sftp, ["smf1-eev-40-sr1.prod.twitter.com"])]

    timeout = 60 * 30 # 30 minutes

    for r in results:
        print(r.get(timeout=timeout))


if __name__ == '__main__':
    main()
