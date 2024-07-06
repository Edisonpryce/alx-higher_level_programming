#!/usr/bin/python3
"""Post request taking url and email
Usage(cmd): ./6-post_email.py <URL> <email>
    - Showing the response
"""
from request import post
import sys


def main():
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = post(url, data=value)
    print(r.text)


if __name__ == '__main__':
    main()
