#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
"""

import requests
from collections import defaultdict


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    if after:
        url += f"?after={after}"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                words = title.split()
                for word in word_list:
                    if word.lower() in words:
                        counts[word.lower()] += words.count(word.lower())

            after = data['data']['after']

            if after:
                return count_words(subreddit, word_list, counts, after)
            else:
                print_counts(counts)
                return counts

        except (KeyError, ValueError):
            return None
    else:
        return None


def print_counts(counts):
    sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
