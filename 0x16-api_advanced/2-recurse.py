#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            if not posts:
                return hot_list

            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']

            return recurse(subreddit, hot_list, after)

        except (KeyError, ValueError):
            return None
    else:
        return None
