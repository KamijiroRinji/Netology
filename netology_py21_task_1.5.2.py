# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
  ]
  
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
  }

# Исправления:

# Сделано - при перемещении несуществующего документа, он добавляется в directories, а в documents - нет. Либо надо сразу его везде добавлять, либо говорить, что такого документа нет; 

# Сделано - при перемещении документа на несуществующую полку программа падает с ошибкой, необходимо исправить аналогично подобной ситуации с добавлением документа; 

# Сделано - когда мы добавляем полку, которая уже существовала ранее, то мы просто потеряем все данные, которые на ней были, это некорректное поведение. Давайте поправим эти моменты, чтобы все было идеально :) 

# + Исправила удаление - теперь проверяет наличие документа в каталоге :)

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def discard():
  number = input('Введите номер документа: ')
  doc_numbers = [document['number'] for document in documents]
  if number in doc_numbers:
    for document in documents:
      if number == document['number']:
        documents.remove(document)
    for key, value in directories.items():
      if number in value:
        value.remove(number)
    print('Документ удалён.')
  else:
    print('Документ с таким номером отсутствует.')

# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
def move():
  number = input('Введите номер документа: ')
  doc_numbers = [document['number'] for document in documents]
  if number not in doc_numbers:
    print('Документ с таким номером отсутствует. Перезапустите программу и введите "a" для добавления нового документа.')
    exit()
  else:
    target_shelf = input('Введите номер полки, на которую нужно перенести документ: ')
    for key, value in directories.items():
      if number in value:
        value.remove(number)
    if target_shelf in directories.keys():
      directories[target_shelf].append(number)
      print('Документ перемещён на полку {}.'.format(target_shelf))
      print(directories)
    else:
      directories[target_shelf] = [number]
      print('Документ перемещён на новую полку {}.'.format(target_shelf))
      print(directories)

# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
def add_shelf():
  new_shelf = input('Введите номер новой полки: ')
  if new_shelf in directories.keys():
    print('Полка с таким номером уже присутствует. Перезапустите программу и введите "s" для поиска по полкам.')
    exit()
  else:
    directories[new_shelf] = []
    print('Создана новая полка {}.'.format(new_shelf))
    print(directories)
  
def doc_work():
  command = input('Введите команду: ')
  if command == 'd':
    discard()
  elif command == 'm':
    move()
  elif command == 'as':
    add_shelf()
  else:
    print('Такая команда отсутствует.\nДоступны комманды:\nd - удалить документ из каталога и убрать с полки,\nm - переместить документ,\nas - добавить полку.\nПожалуйста, перезапустите программу и введите одну из доступных комманд.')

doc_work()
