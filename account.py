__author__ = 'idclark'
import requests


def user_login(user_name, password, bot_desc):
    """ user_name: a valid reddit username
    password: the respective password to the user name
    bot_desc: the name of the bot to be used in the header dict """

    user_information = {'user': user_name,
                        'passwd': password,
                        'api_type': 'json'}

    headers = {'user-agent': str(bot_desc), }

    client = requests.session()
    client.headers = headers
    response = client.post(r'http://www.reddit.com/api/login', data=user_information)

    if response.json()['json']['errors']:
        error_dict = response.json()['json']['errors']
        raise Exception('Error: '+error_dict[0][0])

    client.user = user_name
    return client


def register_account():
    pass


def delete_account():
    pass


def current_account_info(client):
    """
    client: the client created from the user_login() function.
            returns json
    """
    response = client.get(r'http://www.reddit.com/api/me.json')
    acc_info = response['data']
    if not acc_info:
        raise Exception('No data found, Please login')
    return acc_info



