import requests


def number_of_subscribers(subreddit):
    # Set the URL for the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set headers to have a custom User-Agent to avoid being blocked by Reddit's API for having a default User-Agent
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the subreddit is valid and not a redirect
    if response.status_code == 200:
        # Parse the JSON response and return the subscriber count
        return response.json()['data']['subscribers']
    else:
        # If the subreddit is not valid, return 0
        return 0
