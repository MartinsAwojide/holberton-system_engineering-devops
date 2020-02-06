#!/usr/bin/python3
""" A module that works with the Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number os subscribers to a subreddit"""
    try:
        url = 'https://www.reddit.com/r/' + sys.argv[1] + '/about.json'
        header = {'User-agent': 'joonxo'}
        resp = requests.get(url, headers=header).json()
        return (resp.get('data').get('subscribers'))
    except:
        return 0
