import csv
from pymongo import MongoClient

client = MongoClient()

tickets_db = client["tickets_db"]


def read_data(db, csv_file):
    """
    Загрузить данные в бд из CSV-файла
    """
    tickets = []
    with open(csv_file, encoding='utf8') as csv_file:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csv_file)
        for line in reader:
            tickets.append({
                "Исполнитель": line["Исполнитель"],
                "Цена": int(line["Цена"]),
                "Место": line["Место"],
                "Дата": line["Дата"]
            })
    results = db.tickets.insert_many(tickets)
    return results.inserted_ids


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    sorted_tickets = list(db.tickets.find().sort([("Цена",  1)]))
    return sorted_tickets


def find_by_name(db, name):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    special_symbols = ["[", "]", "\\", "/", "^", "$", ".", "|", "?", "*", "+", "(", ")", "{", "}"]
    for special_symbol in special_symbols:
        if special_symbol in name:
            name = name.replace(special_symbol, "\\" + special_symbol)

    tickets = list(db.tickets.find({"Исполнитель": {"$regex": name, "$options": "i"}}).sort([("Цена",  1)]))
    return tickets


if __name__ == "__main__":
    read_data(tickets_db, "artists.csv")
    sorted_tickets = find_cheapest(tickets_db)
    print(sorted_tickets)
    found_tickets = find_by_name(tickets_db, "Seconds to")
    print(found_tickets)
