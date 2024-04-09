#!/usr/bin/python3
"""Contains the recurse function"""
import requests


def recurse(subreddit, aft=None):
    """returns a list containing the titles of all
    hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None."""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/123.0.0.0 Safari/537.36'
        }
    after_param = {'after': '' if aft is None else aft}
    titles_list = []
    res = requests.get(url, headers=headers, params=after_param)
    if res.status_code == 200:
        for k in res.json().get('data').get('children'):
            titles_list.append(k.get('data').get('title'))

        after = res.json().get('data').get('after')
        if after is None:
            titles_list.extend(recurse(subreddit, after))
        return titles_list
    else:
        return None
