__author__ = 'idclark'
import requests as r


def about_subreddit(sr):
    """get an overview for a given subreddit
       > running = about_subreddit('running')
    """

    url = r'http://www.reddit.com/r/{sr}/about.json'.format(sr=sr)
    response = r.get(url)
    return response.json()['data']


def my_subreddits(client, status, limit):
    """
    return a list of subreddits an account is subscribed to.
    client requires running accounts.user_login() first to start a user session
     status: 'subscriber', 'moderator', 'contributor'
     limit: max of 100

     > my_subs = my_subreddits(client, 'contributor', limit=25)
    """
    url = r'http://www.reddit.com/subreddits/mine/{st}.json'.format(st=status)
    data = {'limit': limit}
    response = client.get(url, data=data)
    return response.json()['data']


#TODO this returns 404 ??
def recommend_subreddits(srnames, omit):
    """
    Inputs: srnames = comma sep list of subreddits
    omit: subreddits to ommit from the reccommendation
    """
    data = {'srnames': ",".join(srnames), 'omit': ",".join(omit)}
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
    return response.json()['data']


def subreddits_by_rank(criteria, limit=3):
    """
    returns list of subreddits according to given criteria
    criteria: popular, new, banned

    > most_popular_subs = subreddits_by_rank('popular', limit=10)
    """
    data = {'limit': limit}
    url = r'http://www.reddit.com/subreddits/{c}.json'.format(c=criteria)
    response = r.get(url, data=data)
    return response.json()['data']['children']


def list_subreddit_submissions(subreddit, criteria):
    """
    for a given subreddit, return a list of articles, sorted by the given criteria:
    hot, new, random

    > python_subs = list_subreddit_submissions('python', 'hot')
    """
    criteria_choices = ['hot', 'new', 'random']
    if criteria not in criteria_choices:
        raise Exception('Please enter a valid criteria choice')
    url = r'http://www.reddit.com/r/{s}/{c}.json'.format(s=subreddit, c=criteria)
    response = r.get(url)
    data = response.json()
    children = data['data']['children']
    return children

