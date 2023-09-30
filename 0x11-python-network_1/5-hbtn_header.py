#!/usr/bin/python3
"""
script that sends request to URL and
displays value of a variable in response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    x_r_id = response.headers.get('X-Request-Id')

    if x_r_id is not None:
        print(x_r_id)
