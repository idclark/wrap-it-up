__author__ = 'idclark'
import requests as r

#TODO this returns 404
def comments_from_article(subreddit, article, sort):
    """
    return the comments for a given subreddit and article
    user can sort by:
    confidence, top, new, hot, controversial, old, random

    > comments = comments_from_article('python', 'that_cool_submission', 'top')
    """
    sorts = ['confidence', 'top', 'new', 'hot', 'controversial', 'old', 'random']
    if sort not in sorts:
        raise Exception('Please select a valid sort criteria')
    url = r'http://www.reddit.com/r/{s}/comments/{a}.json'.format(s=subreddit, a=article)
    data = {'sort': sort}
    response = r.get(url, data=data)
    return response.json()


