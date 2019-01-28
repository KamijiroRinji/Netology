def get_cook_book_from_file():
	cook_book = {}
	with open('cook_book.txt') as f:
		for line in f:
			count = 0
			dish_name = line.lower().rstrip()
			ingredient_count = int(f.readline())
			dish_ingredients = []
			while count < ingredient_count:
				ingredient = {}
				read_ingredient = f.readline().lower().rstrip().split(' | ')
				ingredient['ingredient_name'] = read_ingredient[0]
				ingredient['quantity'] = int(read_ingredient[1])
				ingredient['measure'] = read_ingredient[2]
				dish_ingredients.append(ingredient)
				count += 1
			f.readline()
			cook_book[dish_name] = dish_ingredients
	return cook_book

def get_shop_list_by_dishes(dishes, person_count):
	cook_book = get_cook_book_from_file()
	shop_list = {}
	for dish in dishes:
		for ingridient in cook_book[dish]:
			new_shop_list_item = dict(ingridient)

			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingredient_name'] not in shop_list:
				shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
	return shop_list

def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
	person_count = int(input('Введите количество человек: '))
	dishes = input('Введите блюда в расчете на одного человека (через запятую без пробелов): ') \
	.lower().split(',')
	shop_list = get_shop_list_by_dishes(dishes, person_count)
	print_shop_list(shop_list)

create_shop_list()
