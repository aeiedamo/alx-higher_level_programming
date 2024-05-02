#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys

    username, password = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(username, password))
    json = res.json()
    print(json.get("id"))
