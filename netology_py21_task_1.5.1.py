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

# Сделано - при поиске владельца несуществующего документа выполнение программы у вас просто прерывается, лучше выводить соотвествующее предупреждение пользователю. 

# Сделано - Аналогично при поиске полки несуществующего документа; 

# Сделано - при добавлении нового документа на ранее несуществующую полку ваша программа падает с ошибкой. Это нежелательно, лучше либо вообще ничего не делать и выводить предупреждение, либо сразу добавлять эту новую полку; 

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;  
def people():
  number = input('Введите номер документа: ')
  doc_numbers = [document['number'] for document in documents]
  if number in doc_numbers:
    for document in documents:
      if number == document['number']:
        print('Владелец документа: {}.'.format(document['name']))
  else:
    print('Документ с таким номером отсутствует.')

# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"; 
def llist():
  print('Список документов:')
  for document in documents:
    print('{} {} {}'.format(document['type'], document['number'], document['name'])) 
  
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf():
  number = input('Введите номер документа: ')
  doc_numbers = [document['number'] for document in documents]
  if number in doc_numbers:
    for key, value in directories.items():
      if number in value:
        print('Документ находится на полке {}.'.format(key))
  else:
    print('Документ с таким номером отсутствует.')
      
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add():
  number = input('Введите номер документа: ')
  doc_numbers = [document['number'] for document in documents]
  if number in doc_numbers:
    print('Документ с таким номером уже присутствует в каталоге. Перезапустите программу и введите "p" для поиска по каталогу.')
    exit()
  doc_type = input('Введите тип документа: ')
  name = input('Введите имя владельца документа: ')
  shelf_number = input('Введите номер полки, на которой будет храниться документ: ')

  newdoc = {'type': doc_type, 'number': number, 'name': name}
  documents.append(newdoc)
  
  if shelf_number in directories.keys():
    directories[shelf_number].append(number)
    print('Документ добавлен в каталог и на полку {}.'.format(shelf_number))
  else:
    directories[shelf_number] = [number]
    print('Документ добавлен в каталог и на новую полку {}.'.format(shelf_number))

def doc_work():
  command = input('Введите команду: ')
  if command == 'p':
    people()
  elif command == 'l':
    llist()
  elif command == 's':
    shelf()
  elif command == 'a':
    add()
  else:
    print('Такая команда отсутствует.\nДоступны комманды:\np - найти владельца документа,\nl - вывести список всех документов,\ns - найти полку, на которой находится документ,\na - добавить документ в каталог и на полку.\nПожалуйста, перезапустите программу и введите одну из доступных комманд.')

doc_work()
