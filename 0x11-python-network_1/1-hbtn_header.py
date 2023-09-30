#!/usr/bin/python3
"""
Script that takes in a URL, sends request & displays
the value of X-Request-Id variable found in header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
