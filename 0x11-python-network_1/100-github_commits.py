#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    own = sys.argv[2]
    commits = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(own, repo)
    )
    commits = commits.json()
    counter = 0

    for commit in commits:
        sha256 = commit.get("sha")
        auth = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha256, auth))
        counter += 1
        if counter >= 9:
            break
