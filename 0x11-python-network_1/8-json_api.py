#!/usr/bin/python3
"""
Python script sends a POST request to URL and
to an URL with letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except IndexError:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except ValueError:
        print("Not a valid JSON")