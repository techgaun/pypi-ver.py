#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import requests
import sys
from distutils.version import StrictVersion

def get_versions(pkg_name):
    url = "https://pypi.python.org/pypi/%s/json" % (pkg_name)
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        data = response.json()
        versions = data["releases"].keys()
        versions.sort(key=StrictVersion, reverse=True)
    else:
        versions = ["No such package found"]
    return versions

if len(sys.argv) == 1:
    print "Usage: %s <package_name>" % (sys.argv[0])
    sys.exit(1)
print "\n".join(get_versions(sys.argv[1]))
