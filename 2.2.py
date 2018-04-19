
# 1. Считать и декодировать файл
# 2. Посчитать повторения
# 3. Выделить длинные слова
# 4. Выделить топ-10 и вывести его

import chardet

def main():
    files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsfr.txt']
    for file in files:
        print('Top-10 most frequent words in "{}"'.format(file.name))
        top10_words_by_occurancies()

def read_and_decode():
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
    return s

def count_occurancies():
    words = read_and_decode()
    list_of_words = words.lower().replace('\n', ' ').split(' ')
    count_words = [(word, list_of_words.count(word)) for word in set(list_of_words)]
    return count_words

def pick_long_words():
    count_words = count_occurancies()
    long_words = []
    for word, occurancies in count_words:
        if len(word) > 6:
            long_words.append((word, occurancies))
    return long_words

def top10_words_by_occurancies():
    long_words = pick_long_words()
    long_words.sort(key = lambda word: word[1], reverse = True)
    top_long_words = long_words[:10]
    for word, occurancies in top_long_words:
        print(word, occurancies)


