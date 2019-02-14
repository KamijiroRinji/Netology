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


if __name__ == "__main__":
    user_uid = input('Введите числовой идентификатор пользователя: ')
    try:
        user_uid = int(user_uid)
    except ValueError:
        print('Пожалуйста, перезапустите программу и введите именно ЧИСЛОВОЙ идентификатор пользователя!')
        exit()

    user = User(TOKEN, user_uid)

    def print_decorator(print_function):
        def wrapped_function(*args, **kwargs):
            return print_function("https://vk.com/id" + str(user.uid))

        return wrapped_function
    print = print_decorator(print)

    print(user)
