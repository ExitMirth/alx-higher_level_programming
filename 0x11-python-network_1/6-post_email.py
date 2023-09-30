#!/usr/bin/python3
"""
script that takes in URL and email address,
sends POST request to passed URL with the email,
and displays body of response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
