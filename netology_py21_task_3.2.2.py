import requests
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
    def __init__(self, token, uid):
        self.token = token
        self.uid = uid

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN
        }

    def __and__(self, other):
        params = self.get_params()
        source_uid = self.uid
        if not source_uid:
            pass
        else:
            try:
                params['source_uid'] = int(source_uid)
            except ValueError:
                print('Пожалуйста, перезапустите программу и введите ЧИСЛОВОЙ идентификатор пользователя!')
                exit()
        target_uid = other.uid
        try:
            params['target_uid'] = target_uid
        except ValueError:
            print('Пожалуйста, перезапустите программу и введите ЧИСЛОВОЙ идентификатор пользователя!')
            exit()
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()['response']


if __name__ == "__main__":
    user1_uid = input('Введите числовой идентификатор пользователя, для которого необходимо искать общих друзей: ')
    if not user1_uid:
        pass
    else:
        try:
            user1_uid = int(user1_uid)
        except ValueError:
          print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
          exit()
    try:
        user2_uid = int(input('Введите числовой идентификатор пользователя, с которым необходимо искать общих друзей: '))
    except ValueError:
        print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
        exit()

    user1 = User(TOKEN, user1_uid)
    user2 = User(TOKEN, user2_uid)
    mutual_friends_class_objects = []
    for friend in user1 & user2:
        user = User(TOKEN, friend)
        mutual_friends_class_objects.append(user)
    print('Общие друзья:\n', mutual_friends_class_objects)
