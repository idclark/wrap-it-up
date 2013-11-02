__author__ = 'idclark'
import users as u


def test_get_user_activity_submit():
    activity = u.get_user_activity('submitted', 'Wonnk13-1')
    assert activity == []


def test_get_user_activity_comment():
    comments = u.get_user_activity('comments', 'Wonnk13-1')
    real_comments = u.get_user_activity('comments', 'Wonnk13')
    assert comments == []
    assert real_comments != []


def test_about_user():
    overview = u.about_user('Wonnk13-1')
    assert overview['comment_karma'] == 0
    assert overview['name'] == 'Wonnk13-1'
