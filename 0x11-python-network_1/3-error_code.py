#!/usr/bin/python3
"""request sent to a given URL and shows the response body.
Usage(cmd): ./3-error_code.py <URL>
  - Takes care of HTTP errors.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


def main():
    url = sys.argv[1]

    request = Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    main()
