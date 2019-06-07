from data.data import documents, directories
from logger.logger import logger


# p – get_name_by_number – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
@logger('log.txt')
def get_name_by_number():
    number = input('Введите номер документа: ')
    doc_numbers = [document['number'] for document in documents]
    if number in doc_numbers:
        for document in documents:
            if number == document['number']:
                print('Владелец документа: {}.'.format(document['name']))
    else:
        print('Документ с таким номером отсутствует.')


# l – get_documents – команда, которая выведет список всех документов
# в формате passport "2207 876234" "Василий Гупкин";
@logger('log.txt')
def get_all_documents():
    print('Список документов:')
    for document in documents:
        print('{} {} {}'.format(document['type'], document['number'], document['name']))


# s – get_directory_by_number – команда, которая спросит номер документа и выведет номер полки,
# на которой он находится;
@logger('log.txt')
def get_directory_by_number():
    number = input('Введите номер документа: ')
    doc_numbers = [document['number'] for document in documents]
    if number in doc_numbers:
        for key, value in directories.items():
            if number in value:
                print('Документ находится на полке {}.'.format(key))
    else:
        print('Документ с таким номером отсутствует.')


# a – add_document – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
@logger('log.txt')
def add_document():
    number = input('Введите номер документа: ')
    doc_numbers = [document['number'] for document in documents]
    if number in doc_numbers:
        print(
            'Документ с таким номером уже присутствует в каталоге. '
            'Перезапустите программу и введите "p" для поиска по каталогу.')
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


@logger('log.txt')
def doc_work():
    command = input('Введите команду: ')
    if command == 'p':
        get_name_by_number()
    elif command == 'l':
        get_all_documents()
    elif command == 's':
        get_directory_by_number()
    elif command == 'a':
        add_document()
    else:
        print(
            'Такая команда отсутствует.\nДоступны комманды:\np - найти владельца документа,\n'
            'l - вывести список всех документов,\ns - найти полку, на которой находится документ,\n'
            'a - добавить документ в каталог и на полку.\n'
            'Пожалуйста, перезапустите программу и введите одну из доступных комманд.')


get_name_by_number()
get_all_documents()
get_directory_by_number()
add_document()

doc_work()
