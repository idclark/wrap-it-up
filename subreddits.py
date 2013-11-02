__author__ = 'idclark'
import requests as r


def about_subreddit(sr):
    """get an overview for a given subreddit"""

    url = r'http://www.reddit.com/r/{sr}/about.json'.format(sr=sr)
    response = r.get(url)
    return response.json()


def my_subreddits(status, limit):
    """
    return a list of subreddits for your account.
     status: 'subscriber', 'moderator', 'contributor'
     limit: max of 100
    """
    url = r'http://www.reddit.com/subreddits/mine/{st}.json'.format(st=status)
    data = {'limit': limit}
    response = r.get(url, data=data)
    return response.json()


#this returns 404 ??TODO
def recommend_subreddits(srnames, omit):
    """
    Inputs: srnames = comma sep list of subreddits
    omit: subreddits to ommit from the reccommendation
    """
    data = {'srnames': list(srnames), 'omit': list(omit)}
    url = r'http://www.reddit.com/api/subreddit_recommendations'
    response = r.get(url, data=data)
    return response.content

#TODO this returns an empty list...
def search_by_topic(query):
    """
    search subreddits by inputting a given topic
    """
    data = {'query': str(query)}
    url = r'http://www.reddit.com/api/subreddits_by_topic.json'
    response = r.get(url, data=data)
    return response.json()


def subreddit_by_rank(criteria, limit):
    """
    returns list of subreddits according to given criteria
     popular, new, banned
    """
    data = {'limit': limit}
    url = r'http://www.reddit.com/subreddits/{c}.json'.format(c=criteria)
    response = r.get(url, data)
    return response.json()


def subreddit_listings(subreddit, criteria):
    """
    for a given subreddit, return a list of articles, sorted by the given criteria:
    hot, new, random
    """
    criteria_choices = ['hot', 'new', 'random']
    if criteria not in criteria_choices:
        raise Exception('Please enter a valid criteria choice')
    url = r'http://www.reddit.com/r/{s}/{c}.json'.format(s=subreddit, c=criteria)
    response = r.get(url)
    return response.json()

