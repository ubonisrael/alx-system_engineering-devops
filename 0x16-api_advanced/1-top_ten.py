#!/usr/bin/python3
"""A module that contains the 'number_of_subscribers' function"""
import requests


def top_ten(subreddit):
    """Fetches the first 10 titles of the hottest posts on a subreddit"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/123.0.0.0 Safari/537.36'
        }
    res = requests.get(url, headers=headers, params={'limit': 10})
    if res.status_code == 200:
        for k in res.json().get('data').get('children'):
            print(k.get('data').get('title'))
    else:
        print(None)
