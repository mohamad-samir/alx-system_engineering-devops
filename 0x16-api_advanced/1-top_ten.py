#!/usr/bin/python3
"""
1-top_ten.py
"""

import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'custom user agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'])
