import chardet

files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']

for file in files:
  with open(file, 'rb') as f:
    data = f.read()
    result = chardet.detect(data)
    s = data.decode(result['encoding'])
    list_of_words = s.lower().replace('\n', ' ').split(' ')
    count_words = [(word, list_of_words.count(word)) for word in set(list_of_words)]
    long_words = []
    for word, occurancies in count_words:
      if len(word) > 6:
        long_words.append((word, occurancies))
    long_words.sort(key = lambda word: word[1], reverse = True)
    top_long_words = long_words[:10]
    print('Top-10 most frequent words in "{}":'.format(f.name))
    for word, occurancies in top_long_words:
      print(word, occurancies)
