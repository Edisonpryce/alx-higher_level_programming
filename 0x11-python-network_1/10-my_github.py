#!/usr/bin/python3
"""Get request to a given url
Usage(cmd): ./7-error_code.py <URL>
    - http error been handled
"""
from request import get
from requests.auth import HTTPBasicAuth
import sys


def main():
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))


if __name__ == '__main__':
    main()
