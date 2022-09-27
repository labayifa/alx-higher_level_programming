#!/usr/bin/python3
""" Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
- Print the response body encode utf-8
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
