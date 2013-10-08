import requests


def user_login(user_name, password, bot_desc):
    """
    user_name: a valid reddit username
    passwork: the respective password to the user name
    bot_desc: the name of the bot to be used in the header dict
    """
    user_information = {'user' : user_name,
                        'passwd' : password,
                        'api_type' : 'json'}

    headers = {'user-agent': str(bot_desc),}

    client = requests.session()
    client.headers=headers
    response = client.post(r'http://www.reddit.com/api/login',data=user_information)

    if response.json()['json']['errors']:
        error_dict = response.json()['json']['errors']
        raise Exception('Error: '+ error_dict[0][0])
    

    

    

    
    
    

    


    
