import requests

def get_subreddit_info(client, limit, sr, sort, **kwargs):
    """client: a user_login() session
       limit: num of stories returned from 1:100
       sr: subreddit or serries using +
       sort: top, hot, or new
       **kwargs: unknown params """

    params = {'limit' : limit}.update(kwargs)
    url = r'http://www.reddit.com/r/{sr}/{sort}.json'.format(sr=sr, sort=sort)
    r = client.get(url, params=params)
    r.json()
    return r.json()
