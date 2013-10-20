wrap-it-up
==========

Toy python wrapper as I experiment with the [http://www.reddit.com/dev/api][Official Reddit API]
It's not intended to compete with or be as comprehensive as [https://praw.readthedocs.org/en/latest/][PRAW]

Usage
===========
The package is broken down into modules following the structure of the API.
Brief overview:

Accounts
--------
login, create and delete user accounts.

`client = user_login('your_username', 'your_password')`

`your_overview = current_account_overview(client)`

Users
-------
Retrieve the activity of a given Reddit account, options include: overview, submissions, comments and likes

`user_submissions = get_user_activity('submitted', 'valid_username', 'top', 100, 'year')`

Subreddits
------------
Retrieve info about a given, or all subreddits of a logged in client. More to come

`python_overview = about_subreddit('python')`

