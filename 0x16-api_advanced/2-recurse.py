#!/usr/bin/python3
"""
2-recurse.py
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    # Define the URL for the Reddit API with the specified subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Define the user-agent header for the HTTP request
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Define the parameters for the HTTP request,
    # including the 'after' parameter
    params = {'after': after}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the response status code is not 200 (indicating an error)
    if response.status_code != 200:
        return None

    # Parse the JSON data from the response
    data = response.json()

    # Extract the list of posts from the JSON data
    posts = data['data']['children']

    # Iterate through the posts and add their titles to the hot_list
    for post in posts:
        hot_list.append(post['data']['title'])

    # Get the 'after' value from the JSON data
    after = data['data']['after']

    # If there is a valid 'after' value, recursively call the
    # function with the updated 'after'
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        # If there is no 'after' value (reached the end of the list),
        # return the hot_list
        return hot_list
