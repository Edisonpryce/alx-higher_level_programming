#!/usr/bin/python3
"""Get request to a given url
Usage(cmd): ./7-error_code.py <URL>
    - http error been handled
"""
from request import get
import sys


def main():
    url = sys.argv[1]

    r = get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == '__main__':
    main()
