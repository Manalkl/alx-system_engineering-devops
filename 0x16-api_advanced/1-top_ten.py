#!/usr/bin/python3
"""this is function file"""


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    data = requests.get(url,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        allow_redirects=False)

    if data.status_code != 200:
        print("None")
        return

    data = data.json()['data']['children']

    if len(data) == 0:
        print("None")
        return

    for x in data:
        print(x['data']['title'])
