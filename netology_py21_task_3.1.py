import requests
import chardet

def get_source_file_path():
  source_file_path = input('\nEnter the full path to the source file: ')
  return source_file_path

def get_result_file_path():
  result_file_path = input('\nEnter the full path to the result file: ')
  return result_file_path

def read_and_decode():
  source_file_path = get_source_file_path()
  with open(source_file_path, 'rb') as source:
    data = source.read()
    result_enc = chardet.detect(data)
    result_text = data.decode(result_enc['encoding'])
  return result_text

def fill_data():
  source_text = read_and_decode()
  data = {'text': source_text}
  return data

def put_langs_to_params():
  initial_lang = input('\nTranslate from: ')
  result_lang = input('\nTranslate to: ')
  params = {'lang': f'{initial_lang}-{result_lang}', 'srv': 'tr-text', 'id': 'f5c948f1.5c59b9e9.16d39b90-6-0'}
  return params

def get_translation():
  data = fill_data()
  params = put_langs_to_params()
  URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
  if len(data['text']) > 650:
    data_list = [data['text'][i: i+650] for i in range(0, len(data['text']), 650)]
    data_translated = []
    for piece in data_list:
      resp = requests.get(URL, data={'text': piece}, params=params)
      data_translated.append(resp.json()['text'][0])
    return ''.join(data_translated)
  else:
    resp = requests.get(URL, data=data, params=params)
    return resp.json()['text'][0]

def write_translation():
  translation = get_translation()
  result_file_path = get_result_file_path()
  with open(result_file_path, 'w') as result:
    result.write(translation)
  return result_file_path

def main():
  print("Hello there!\n\nA little hint on language codes:\n 'de' stands for German,\n 'es' for Spanish,\n 'fr' for French\n and 'ru' stands for Russian.\n")
  try:
    more_files = input('Need to translate a file? (y/n) ')
    while more_files == 'y':
      result_file_path = write_translation()
      print('\nThe translation is done and written to {}.'.format(result_file_path))
      more_files = input('\nMore files to translate? (y/n) ')
  except KeyError:
    print("\nJust a kindly reminder on language codes:\n 'de' stands for German,\n 'es' for Spanish,\n 'fr' for French\n and 'ru' stands for Russian.\nPlease, restart the program and enter one of the supported codes.")
    exit()

main()
