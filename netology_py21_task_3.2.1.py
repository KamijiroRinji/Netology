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

TOKEN = '7679714c6b33062d56bb9406d5a531fac2cee244ebe947c3b298bf993b7528ca1f56e9403aee599048352'

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
      target_uid = int(input('Введите числовой идентификатор пользователя, с которым необходимо искать общих друзей: '))
      try:
        params['target_uid'] = target_uid
      except ValueError:
        print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
        exit()
      response = requests.get('https://api.vk.com/method/friends.getMutual', params)
      if not source_uid:
        return [friends_ids_and_names[friend] for friend in response.json()['response']]
      else:
        return response.json()['response']

user = User(TOKEN)
pprint(user.get_mutual_friends())
