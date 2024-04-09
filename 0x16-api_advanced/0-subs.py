#!/usr/bin/python3
"""A module that contains the 'number_of_subscribers' function"""
import requests


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers on the subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'ubuntu:0x16.advanced_api/v1'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    subs = res.json().get('data').get('subscribers')
    return subs
