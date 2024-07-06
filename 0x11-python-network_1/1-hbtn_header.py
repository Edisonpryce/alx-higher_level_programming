#!/usr/bin/python3
"""Displays a given URL X-Request-Id header.
Usage(cmd): ./1-hbtn_header.py <URL>
"""
from urllib.request import Request, urlopen
import sys


def main():
    url = sys.argv[1]

    request = Request(url)
    with urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == '__main__':
    main()
