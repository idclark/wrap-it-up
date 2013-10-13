__author__ = 'idclark'
import requests

def get_user_overview(client, user, sort='top', limit=25, t=all):
    """

    """
    user_information = {'user': user, 'sort': sort, 'limit': limit, 't': str(t)}
    url = r'http://www.reddit.com/api/{u}/overview.json'.format(u=user)
    response = client.get(url, data=user_information)
    overview = response.content
    return overview


def get_user_submissions(client, user, sort='top', limit=25, t=all):
    """

    """
    user_information = {'user': user, 'sort': sort, 'limit': limit, 't': str(t)}
    url = r'http://www.reddit.com/api/{u}/submitted.json'.format(u=user)
    response = client.get(url, data=user_information)
    submissions = response.content
    return submissions


def get_user_comments(client, user, sort='top', limit=25, t=all):
    """

    """
    user_information = {'user': user, 'sort': sort, 'limit': limit, 't': str(t)}
    url = r'http://www.reddit.com/api/{u}/comments.json'.format(u=user)
    response = client.get(url, data=user_information)
    comments = response.content
    return comments
