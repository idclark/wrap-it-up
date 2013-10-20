__author__ = 'idclark'
import requests as r


def about_subreddit(sr):
    """get an overview for a given subreddit"""

    url = r'http://www.reddit.com/r/{sr}/about.json'.format(sr=sr)
    response = r.get(url)
    return response.content


def my_subreddits(status, limit):
    """
    return a list of subreddits for your account.
     status: 'subscriber', 'moderator', 'contributor'
     limit: max of 100
    """
    url = r'http://www.reddit.com/subreddits/mine/{st}.json'.format(st=status)
    data = {'limit': limit}
    response = r.get(url, data=data)
    return response.content

