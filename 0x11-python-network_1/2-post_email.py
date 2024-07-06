#!/usr/bin/python3
"""POST request to a given URL with an email.
Usage(cmd): ./2-post_email.py <URL> <email>
  - This shows the response body.
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


def main():
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlencode(value).encode("ascii")

    request = Request(url, data)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == '__main__':
    main()
