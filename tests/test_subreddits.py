__author__ = 'idclark'

import subreddits as s
import accounts as a

client = a.user_login(user_name='Wonnk13-1', password='password', bot_desc='foobar')


def test_about_subreddits():
    running_info = s.about_subreddit('running')
    #case sensitive? a: nope
    Running_info = s.about_subreddit('Running')
    assert 'subscribers' in running_info.keys()
    assert Running_info['url'] == '/r/running/'


def test_my_subreddits():
    empty = s.my_subreddits(client=client, status='subscriber', limit=1)
    #do you need a username- yup- sign in
    assert empty['children'] == []


def test_subreddits_by_rank():
    rank = s.subreddits_by_rank('popular', limit=35)
    assert rank[0]['data']['url'] == '/r/pics/'


def test_list_subreddit_submissions():
    running_subs = s.list_subreddit_submissions('running', 'hot')
    assert running_subs[0]['data']['title'] == 'Map of today\'s run with some 70 other people for my country\'s independence day'
