#!/usr/bin/python3
"""Fetching resource from https://alx-intranet.hbtn.io/status."""
from urllib.request import Request, urlopen


def main():
    request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == '__main__':
    main()
