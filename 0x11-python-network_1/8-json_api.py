#!/usr/bin/python3
"""POST request sent to http://0.0.0.0:5000/search_user with a letter.
Usage(cmd): ./8-json_api.py <letter>
"""
import sys
import requests


def main():
    lett = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lett}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__:
    main()
