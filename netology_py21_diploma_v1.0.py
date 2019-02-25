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

    def get_groups_ids(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/groups.get', params)
        return response.json()['response']['items']

    def get_friends_ids(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()['response']['items']

    def get_unique_groups_ids(self):
        params = self.get_params()
        user_groups_ids = self.get_groups_ids()
        friends_ids = self.get_friends_ids()
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
                        time.sleep(3)
                        pass
                    else:
                        pass
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
                    time.sleep(3)
                    pass
                else:
                    pass
        return unique_groups_list

    def write_unique_groups_to_json(self):
        necessary_keys = ("id", "name", "members_count")
        with open('groups.json', 'w') as datafile:
            json.dump([{attr: unique_group[attr] for attr in unique_group if attr in necessary_keys}
                       for unique_group in unique_groups_list], datafile, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    TOKEN = input('Введите токен:\n')
    user_data = input('Вы можете ввести имя (напечатайте "username" без кавычек) '
                      'или числовой идентификатор пользователя (напечатайте "id" без кавычек) '
                      'для вывода его уникальных групп.\nЧто вводим? (username/id)\n')
    if user_data == 'id':
        try:
            user_uid = int(input('Введите числовой идентификатор пользователя,'
                                 ' уникальные группы которого необходимо вывести:\n'))
            user = User(TOKEN, user_uid)
        except ValueError:
            print('Пожалуйста, перезапустите программу и введите имя или ЧИСЛОВОЙ идентификатор пользователя!')
            exit()
        except NameError:
            print('Пожалуйста, перезапустите программу и введите имя или ЧИСЛОВОЙ идентификатор пользователя!')
            exit()
        unique_groups_list = user.get_unique_groups_info()
        user.write_unique_groups_to_json()
        print('Уникальные группы пользователя {} записаны в файл groups.json'.format(user_uid))
    elif user_data == 'username':
        user_name = input('Введите имя пользователя, уникальные группы которого необходимо вывести:\n')
        user = User(TOKEN, user_name)
        unique_groups_list = user.get_unique_groups_info()
        user.write_unique_groups_to_json()
        print('Уникальные группы пользователя {} записаны в файл groups.json'.format(user_name))
    else:
        print('Пожалуйста, перезапустите программу и введите\n'
              '- "имя" для вывода уникальных групп пользователя по его имени\nИЛИ\n'
              '- "id" для вывода уникальных групп пользователя по его числовому идентификатору.')
        exit()
