import json
import chardet

# открыли файл на чтение и десериализовали в переменную json_data, т.е. распаковали json в словарь
def json_to_dict():
  json_file = input('Enter full file name: ')
  try:
    with open(json_file) as datafile:
      json_data = json.load(datafile)
    # print(type(datafile))
  except json.decoder.JSONDecodeError:
    print('Please provide a json file!')
  except FileNotFoundError:
    print('Please provide an existing json file!')
  return json_data

# открыли файл на запись и сериализовали туда нужную часть json_data
def extract_news_items():
  with open('newsafr2.json', 'w') as datafile:
    json_data = json_to_dict()
    json.dump(json_data['rss']['channel']['items'], datafile, ensure_ascii=False, indent=2)

# десериализуем news_items
def news_items_to_dict():  
  extract_news_items()
  with open('newsafr2.json') as datafile:  
    json_data = json.load(datafile)
  return json_data

# записываем сами новости в текстовый файл
def write_to_txt():
  json_data = news_items_to_dict()
  with open('newsafr3.txt', 'w') as datafile:
    for news_piece in json_data:
      datafile.write(news_piece['description'])

# обработка текста

# читаем и декодируем
def read_and_decode():
  write_to_txt()
  with open('newsafr3.txt', 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    s = data.decode(result['encoding'])
  return s

# считаем вхождения
def count_occurancies():
  words = read_and_decode()
  list_of_words = words.lower().replace('\n', ' ').split(' ')
  count_words = [(word, list_of_words.count(word)) for word in set(list_of_words)]
  return count_words

# выбираем только длинные слова
def pick_long_words():
  count_words = count_occurancies()
  long_words = []
  for word, occurancies in count_words:
    if len(word) > 6:
      long_words.append((word, occurancies))
  return long_words

# выбираем топ-10
def top10_words_by_occurancies():
  long_words = pick_long_words()
  long_words.sort(key = lambda word: word[1], reverse = True)
  top_long_words = long_words[:10]
  print('Top-10 most frequent words: ')
  for word, occurancies in top_long_words:
    print(word, occurancies)

def main():
  top10_words_by_occurancies()

main()
