#!/usr/bin/env python
# Author: Rich Mirch @0xm1rch
# Description: Convert SSSD cache files to John The Ripper format
# Tested on: Kali GNU/Linux Rolling 2019.1
#
# Example:
#    ./ssscache2john.py /var/lib/sss/cache_LDAP.ldb
#
# Install dependencies
# apt install sssd-common python-ldb

from __future__ import print_function
import ldb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s <cache.ldb>\n" % sys.argv[0])
        sys.exit(1)

    conn = ldb.Ldb(sys.argv[1])
    for record in conn.search("CN=SYSDB"):
        if "CN=USERS" in str(record.dn).upper():
            for item in record.items():
                if item[0] == "name":
                    username = str(item[1])
                elif item[0] == "cachedPassword":
                    cachedPassword = str(item[1])
            print(username + ":" + cachedPassword)
