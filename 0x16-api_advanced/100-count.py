#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, aft=None, count={}):
    """ a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted
    count of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not)."""
    word_list = [x.lower() for x in word_list]

    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/123.0.0.0 Safari/537.36'
        }
    after_param = {'after': '' if aft is None else aft}
    res = requests.get(url, headers=headers, params=after_param)
    if res.status_code == 200:
        for k in res.json().get('data').get('children'):
            title = [a.lower() for a in k.get('data').get('title').split(' ')]
            for x in word_list:
                if x in title:
                    count[x] = count.get(x, 0) + 1

        after = res.json().get('data').get('after')
        if after is None:
            count_words(subreddit, word_list, after, count)
        else:
            sorted_result = sorted(count.items(), key=lambda x: x[1],
                                   reverse=True)
            new_dict = dict(sorted_result)
            for k, v in new_dict.items():
                print("{}: {}".format(k, v))
