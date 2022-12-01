#!/usr/bin/python3
"""
function that queries the Reddit API
returns the number of subscribers(total)
"""
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns number
        of subscribers
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    else:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2;\
                    Win64; x64) AppleWebKit/537.36 (KHTML,\
                    like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        res = requests.get(url, headers=headers).json()
        return (res.get('data')['subscribers'])
