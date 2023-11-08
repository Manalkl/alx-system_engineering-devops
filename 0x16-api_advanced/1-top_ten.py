#!/usr/bin/python3
"""function that queries the Reddit API and returns
titles of first 10 hot posts
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            posts = data['data']['children']

            if not posts:
                print("No hot posts found.")
                return

            for news, post in enumerate(posts[:10]):
                print(f"{news + 1}. {post['data']['title']}")

        except (KeyError, ValueError):
            print("Error parsing Reddit API response.")
    else:
        print("None")
