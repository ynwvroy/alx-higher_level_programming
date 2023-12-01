#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
You must use the actual package requests
"""
import requests


def main():
    """fetches https://alx-intranet.hbtn.io/status
    You must use the actual package requests
    """
    r = requests.get('https://alx-intranet.hbtn.io/status')
    r.encoding = 'utf-8'
    content = r.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    main()
