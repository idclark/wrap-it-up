import accounts as a

client = a.user_login(user_name='Wonnk13-1', password='password', bot_desc='foo')


def test_user_login():
    assert client.user == 'Wonnk13-1'


def test_current_account_overview():
    overview = a.current_account_overview(client)
    assert 'comment_karma' in overview.keys()
    assert overview['link_karma'] == 1



