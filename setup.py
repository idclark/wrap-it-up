__author__ = 'idclark'
from distutils.core import setup

setup(
    name = 'reddit_py',
    packages = ['reddit_py'], # this must be the same as the name above
    version = '0.1',
    description = 'A lightweight wrapper for interacting with the Reddit API',
    author = 'Ian Clark',
    author_email = 'idclark13@gmail.com',
    url = 'https://github.com/idclark/wrap-it-up',   # use the URL to the github repo
    download_url = 'https://github.com/idclark/wrap-it-up', # I'll explain this in a second
    keywords = ['wrapper', 'reddit'], # arbitrary keywords
    classifiers = [],
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.2"],
    )
