#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    URL = "http://0.0.0.0:5000/search_user"
    data = {"q": sys.argv[1] if len(sys.argv) >= 2 else ""}
    res = requests.post(URL, data)
    type_res = res.headers["content-type"]

    if type_res == "application/json":
        result = res.json()
        iden = result.get("id")
        name = result.get("name")
        if result != {} and iden and name:
            print("[{}] {}".format(iden, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
