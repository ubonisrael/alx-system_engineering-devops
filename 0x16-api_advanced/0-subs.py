#!/usr/bin/python3
"""A module that contains the 'number_of_subscribers' function"""
from requests import get


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers on the subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/111.0.0.4'}
    res = get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    res = res.json()
    return res['data']['subscribers']
