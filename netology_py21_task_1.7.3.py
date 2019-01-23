# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией, выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, что, если у документа нет атрибута name, программа не будет ломаться.

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


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def people():
    number = input('Введите номер документа: ')
    doc_numbers = [document['number'] for document in documents]
    if number in doc_numbers:
        for document in documents:
            if number == document['number']:
                try:
                    print('Владелец документа: {}.'.format(document['name']))
                except KeyError:
                    print('Бесхозный документ.')
    else:
        print('Документ с таким номером отсутствует.')


# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def llist():
    print('Список всех документов:')
    for document in documents:
        try:
            print('{} {} {}'.format(document['type'], document['number'], document['name']))
        except KeyError:
            print('{} {} {}'.format(document['type'], document['number'], 'Нет (бесхозный документ)'))

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
        print(
            'Документ с таким номером уже присутствует в каталоге. Перезапустите программу и введите "p" для поиска по каталогу.')
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
        print(
            'Документ с таким номером отсутствует. Перезапустите программу и введите "a" для добавления нового документа.')
        exit()
    else:
        target_shelf = input('Введите номер полки, на которую нужно перенести документ: ')
        for key, value in directories.items():
            if number in value:
                value.remove(number)
        if target_shelf in directories.keys():
            directories[target_shelf].append(number)
            print('Документ перемещён на полку {}.'.format(target_shelf))
        else:
            directories[target_shelf] = [number]
            print('Документ перемещён на новую полку {}.'.format(target_shelf))


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
def add_shelf():
    new_shelf = input('Введите номер новой полки: ')
    if new_shelf in directories.keys():
        print('Полка с таким номером уже присутствует. Перезапустите программу и введите "s" для поиска по полкам.')
        exit()
    else:
        directories[new_shelf] = []
        print('Создана новая полка {}.'.format(new_shelf))


# o – owners – команда, которая выведет всех владельцев документов;
def list_owners():
    print('Список всех владельцев документов:')
    for document in documents:
        try:
            print('{}'.format(document['name']))
        except KeyError:
            pass


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
    elif command == 'd':
        discard()
    elif command == 'm':
        move()
    elif command == 'as':
        add_shelf()
    elif command == 'o':
        list_owners()
    else:
        print(
            'Такая команда отсутствует.\nДоступны комманды:\np - найти владельца документа,\nl - вывести список всех документов,\ns - найти полку, на которой находится документ,\na - добавить документ в каталог и на полку.\nПожалуйста, перезапустите программу и введите одну из доступных комманд.')


doc_work()
