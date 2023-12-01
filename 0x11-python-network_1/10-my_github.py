#!/usr/bin/python3
"""
Script that actually takes GitHub credentials and uses the GitHub API
to display the user's ID.
"""

import requests
import sys

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    except ValueError:
        print(None)
else:
    print("Usage: ./10-my_github.py <username> <password>")
