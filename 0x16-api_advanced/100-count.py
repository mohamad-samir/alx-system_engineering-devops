#!/usr/bin/python3
"""
2-recurse.py
"""

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    headers = {
        'User-Agent': 'Python/requests:APIproject:version1.0 (by /u/username)'}
    payload = {'after': after}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)

    if response.status_code != 200:
        return None

    if after is None:
        # Base case, when there are no more pages to go through
        sorted_words = sorted(word_count.items(),
                              key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    # Initial setup for word_count dictionary
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    # Get the list of posts
    posts = response.json().get('data').get('children')

    # Count the words in the titles of each post
    for post in posts:
        title = post.get('data').get('title').lower()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    # Get the 'after' value for the next page
    after = response.json().get('data').get('after')

    # Recurse with the next page
    count_words(subreddit, word_list, after, word_count)
