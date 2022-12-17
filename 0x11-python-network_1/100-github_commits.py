#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__name__":
    url = "https://api.github.com/repos/{rails}/{rails}/commits".format(sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[1].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
