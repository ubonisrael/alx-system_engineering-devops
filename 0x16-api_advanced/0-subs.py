#!/usr/bin/python3
"""A module that contains the 'number_of_subscribers' function"""
import requests


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers on the subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/123.0.0.0 Safari/537.36'
        }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        subs = res.json().get('data').get('subscribers')
        return subs
    return 0
