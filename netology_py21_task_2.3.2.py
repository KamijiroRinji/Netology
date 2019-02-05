import xml.etree.ElementTree as ET
import chardet

# получаем имя файла
def get_xml_name():
  xml_name = input('Enter full file name: ')
  return xml_name

# записываем сами новости в текстовый файл
def write_to_txt():
  xml_name = get_xml_name()
  try:
    tree = ET.parse(xml_name)
    root = tree.getroot()
    xml_items = root.findall("channel/item/description")
    with open('newsafr.txt', 'w') as datafile:
      for xml_item in xml_items:
        datafile.write(xml_item.text)
  except ET.ParseError:
    print('Please provide an xml file!')
    exit()
  except FileNotFoundError:
    print('Please provide an existing xml file!')
    exit()

# обработка текста

# читаем и декодируем
def read_and_decode():
  write_to_txt()
  with open('newsafr.txt', 'rb') as f:
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
