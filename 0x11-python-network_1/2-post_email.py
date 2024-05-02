#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode("ascii")
    with urllib.request.urlopen(url, DATA) as res:
        print(res.read().decode("utf-8"))
