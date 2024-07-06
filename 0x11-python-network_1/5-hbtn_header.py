#!/usr/bin/python3
"""Displays a given URL X-Request-Id header.
Usage(cmd): ./5-hbtn_header.py <URL>
"""
from urllib.request import get
import sys


def main():
    url = sys.argv[1]

    r = get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == '__main__':
    main()
