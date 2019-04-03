cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]

def get_dishes_list(dishes):
  cook_book_index = 0
  dishes_index = 0
  while dishes_index < len(dishes):
    cook_book_index = 0
    while cook_book_index < len(cook_book):
      if cook_book[cook_book_index][0] == dishes[dishes_index]:
        dishes[dishes_index] = cook_book[cook_book_index]
        break
      cook_book_index += 1
    dishes_index += 1
  return dishes

def get_shop_list_by_dishes():
  person = int(input('Введите количество человек: '))
  dishes = input('Введите блюда (через запятую без пробелов): ') \
  .lower().split(',')
  dishes = get_dishes_list(dishes)
  dish_index = 0 # Обнуляем счётчик индексов блюд
  ingredient_amount = 0
  while dish_index < len(dishes):
    print(dishes[dish_index][0].capitalize() + ':') # Выводим название блюда
    ingredient_index = 0 # Счётчик индексов ингредиентов
    while ingredient_index < len(dishes[dish_index][1]):
      ingredient_amount = dishes[dish_index][1][ingredient_index][1] * person
      print(dishes[dish_index][1][ingredient_index][0] + ', ' + str(ingredient_amount) + dishes[dish_index][1][ingredient_index][2])
      ingredient_index += 1
    dish_index += 1

get_shop_list_by_dishes()
