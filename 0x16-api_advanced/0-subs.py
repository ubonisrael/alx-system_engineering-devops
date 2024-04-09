#!/usr/bin/python3
"""A module that contains the 'number_of_subscribers' function"""
from requests import get

headers = {'User-Agent': 'Chrome/111.0.0.4'}


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers on the subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    res = get(url, headers=headers)
    if res.status_code == 404:
        return 0
    res = res.json()
    return res['data']['subscribers']
