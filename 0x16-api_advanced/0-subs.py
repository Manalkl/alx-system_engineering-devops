#!/usr/bin/python3
"""function that queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            subscribers = data['data']['subscribers']

            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
