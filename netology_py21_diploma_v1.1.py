import requests
import time
import json

APP_ID = 6859917
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
  'client_id': APP_ID,
  'display': 'page',
  'scope': 'friends, groups, users',
  'response_type': 'token',
  'v': '5.9'
}


class User:
    def __init__(self, token, uid):
        self.token = token
        self.uid = uid

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN
        }

    def get_groups_or_friends_ids(self, groups_or_friends):
        params = self.get_params()
        params['user_id'] = self.uid
        if groups_or_friends == 'groups':
            response = requests.get('https://api.vk.com/method/groups.get', params)
        elif groups_or_friends == 'friends':
            response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()['response']['items']

    def get_user_id_by_id_or_screen_name(self, user_data):
        params = self.get_params()
        params['user_ids'] = user_data
        params['fields'] = 'screen_name'
        response = requests.get('https://api.vk.com/method/users.get', params)
        return response.json()['response'][0]['id']

    def get_unique_groups_ids(self):
        params = self.get_params()
        user_groups_ids = self.get_groups_or_friends_ids('groups')
        friends_ids = self.get_groups_or_friends_ids('friends')
        for friend_id in friends_ids:
            for group_id in user_groups_ids:
                params['group_id'] = group_id
                params['user_id'] = friend_id
                response = requests.get('https://api.vk.com/method/groups.isMember', params)
                print('...')
                try:
                    if response.json()['response'] == 1:
                        user_groups_ids.remove(group_id)
                        break
                except KeyError:
                    if response.json()['error']['error_code'] == 6:
                        time.sleep(1)
        return user_groups_ids

    def get_unique_groups_info(self):
        params = self.get_params()
        params['fields'] = 'members_count'
        unique_groups_ids = self.get_unique_groups_ids()
        unique_groups_list = []
        for group_id in unique_groups_ids:
            params['group_id'] = group_id
            response = requests.get('https://api.vk.com/method/groups.getById', params)
            try:
                unique_groups_list.append(response.json()['response'][0])
            except KeyError:
                if response.json()['error']['error_code'] == 6:
                    time.sleep(1)
        return unique_groups_list

    def write_unique_groups_to_json(self):
        necessary_keys = ('id', 'name', 'members_count')
        with open('groups.json', 'w') as datafile:
            json.dump([{attr: unique_group[attr] for attr in unique_group if attr in necessary_keys}
                       for unique_group in unique_groups_list], datafile, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    TOKEN = input('Введите токен: \n')
    user_name = input('Введите имя или числовой идентификатор пользователя для вывода его уникальных групп: \n')
    try:
        user1 = User(TOKEN, 5279459)
        user1.get_user_id_by_id_or_screen_name(user_name)
        try:
            user_uid = int(user_name)
            user = User(TOKEN, user_uid)
            unique_groups_list = user.get_unique_groups_info()
            user.write_unique_groups_to_json()
            print('Уникальные группы пользователя {} записаны в файл groups.json'.format(user_name))
        except ValueError:
            user1 = User(TOKEN, user_name)
            user_uid = user1.get_user_id_by_id_or_screen_name(user_name)
            user = User(TOKEN, user_uid)
            unique_groups_list = user.get_unique_groups_info()
            user.write_unique_groups_to_json()
            print('Уникальные группы пользователя {} записаны в файл groups.json'.format(user_name))
    except KeyError:
        print('Нет пользователя с таким именем или идентификатором.\n'
              'Пожалуйста, перезапустите программу и введите имя или идентификатор существующего пользователя.')
        exit()
