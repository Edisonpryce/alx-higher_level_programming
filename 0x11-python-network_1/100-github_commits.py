#!/usr/bin/python3
"""GitHub repository 10 most recent commit.

Usage(cmd): ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


def main():
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == '__main__':
    main()
