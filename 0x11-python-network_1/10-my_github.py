#!/usr/bin/python3
"""Get Github User Id based on username and password.

Usage: ./10-my_github.py <username> <pat>
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"

    results = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    if results.get('id') is None:
        print("None")
    else:
        print("{}".format(results.get('id')))

