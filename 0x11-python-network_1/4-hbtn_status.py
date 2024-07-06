#!/usr/bin/python3
"""gets data from https://alx-intranet.hbtn.io/status"""
from urllib.request import get


def main():
    r = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == '__main__':
    main()
