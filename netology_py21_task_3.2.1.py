import requests
from pprint import pprint
from urllib.parse import urlencode

APP_ID = 6859917
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
  'client_id': APP_ID,
  'display': 'page', # popup, mobile
  'scope': 'friends',
  'response_type': 'token',
  'v': '5.9'
}

TOKEN = 'e1993b557e2cf41d0506bfe8f23165e6b319a0f785d7d8220b13f0a1e5d5fd0e366ae6ae174810942fdae'

class User:
  def __init__(self, token):
    self.token = token

  def get_params(self):
    return {
      'v': '5.92',
      'access_token': TOKEN
    }

  def get_friends_ids_and_names(self):
    params = self.get_params()
    params['fields'] = 'nickname'
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_names = {}
    for friend in response.json()['response']['items']:
      friends_names[friend['id']] = f'{friend["first_name"]} {friend["last_name"]}'
    return friends_names
  
  def get_mutual_friends(self):
      friends_ids_and_names = self.get_friends_ids_and_names()
      params = self.get_params()
      source_uid = input('Введите числовой идентификатор пользователя, для которого необходимо искать общих друзей: ')
      if not source_uid:
        pass
      else:
        try:
          params['source_uid'] = int(source_uid)
        except ValueError:
          print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
          exit()
      try:
        target_uid = int(input('Введите числовой идентификатор пользователя, с которым необходимо искать общих друзей: '))
        params['target_uid'] = target_uid
      except ValueError:
        print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
        exit()
      response = requests.get('https://api.vk.com/method/friends.getMutual', params)
      return [friends_ids_and_names[friend] for friend in response.json()['response']]

user = User(TOKEN)
pprint(user.get_mutual_friends())
