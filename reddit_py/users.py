__author__ = 'idclark'
import requests as r


def get_user_activity(activity, user, limit=25, sort='top', time=all):
    """Retrieve a user's activity, choice of:
       Overview, submissions, Comments, liked, disliked, hidden, saved, gilded

       User: a valid reddit username
       limit: a limit on the number of items retrieved, max is 100
       sort: sorting criteria, 'hot', 'top', 'new', 'controversial'
       time: alltime, year, month, day, week, or hour

       > my_activity = get_user_activity('submissions', 'user_name', sort='hot', time='year')
    """
    activity_args = ['overview', 'submitted', 'comments', 'liked', 'disliked', 'hidden', 'saved', 'gilded']
    data = {'activity': activity, 'user': user, 'sort': sort, 'limit': limit, 'time': str(time)}
    if data['activity'] not in activity_args:
        raise Exception('Please enter a correct activity: ' + activity_args)

    url = r'http://www.reddit.com/user/{u}/{a}.json'.format(u=user, a=activity)
    response = r.get(url, data=data)
    return response.json()['data']['children']


def about_user(username):
    """
     retrieve an overview for the given reddit account.

     > user_info = about_user('user_name')
    """

    url = r'http://wwwr.reddit.com/user/{u}/about.json'.format(u=username)
    response = r.get(url)
    return response.json()['data']