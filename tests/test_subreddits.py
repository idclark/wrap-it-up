__author__ = 'idclark'

import subreddits as s


def test_about_subreddits():
    running_info = s.about_subreddit('running')
    #case sensitive? a: nope
    Running_info = s.about_subreddit('Running')
    assert 'subscribers' in running_info.keys()
    assert Running_info['url'] == '/r/running'


def test_my_subreddits():
    empty = s.my_subreddits('subscriber')
    #do you need a username
    #case for Wonnk13
    assert empty == []


def test_subreddits_by_rank():
    rank = s.subredits_by_rank('popular', limit=35)
    assert rank[0] == 'some reddit'


def test_subreddit_list_submissions():
    running_subs = s.subreddit_list_submissions('running', 'hot')
    assert running_subs[0] == 'some string'
