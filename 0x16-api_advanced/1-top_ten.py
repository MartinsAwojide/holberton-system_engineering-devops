#!/usr/bin/python3
""" A module that works with the Reddit API"""
import requests


def top_ten(subreddit):
    """Returns the first 10 hot posts of a subreddit"""
    try:
        url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
        header = {'User-agent': 'joonxo'}
        limit = {'limit': '10'}
        resp = requests.get(url, headers=header,
                            params=limit, allow_redirects=False).json()
        key = resp.get('data').get('children')
        for value in key:
            print(value.get('data').get('title'))
    except:
        print(None)
