boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Daria']

def match_pairs(boys, girls):

  # Сортируем списки

  boys.sort()
  girls.sort()

  # Сначала определяем, у всех ли будет пара, и, если будет, знакомим

  if len(boys) == len(girls):
    pairs = zip(boys, girls) # "Знакомим" пары
    pairs_list = list(pairs) # Преобразовываем zip в список
    print('Идеальные пары:')
    for pair in pairs_list:
      boy, girl = pair # Распаковываем кортеж
      print(boy + ' и ' + girl) # Выводим пару
  else:
    print('Не могу познакомить людей - кто-то может остаться без пары!')

match_pairs(boys, girls)
