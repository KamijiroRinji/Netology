# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
# - Необходимо посчитать общий вес всех животных(экземпляров класса);
# - Вывести название самого тяжелого животного.

import gc

# Сельскохозяйственные животные
class Livestock:
  sound = None
  name = None
  weight = 0

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def feed(self):
    print('nom-nom')
    
  def speak(self):
    print(self.sound)

# Скот для дойки
class Milking_Cattle(Livestock):
  
  def to_milk(self):
    milk = int(input('How much milk did you milk from {}? '.format(self.name)))
    print('The animal is milked, {}l of milk acquired.'.format(milk))
    
class Cow(Milking_Cattle):
  sound = 'moo'
  
class Goat(Milking_Cattle):
  sound = 'bee'

# Скот для стрижки
class Shearing_Cattle(Livestock):

  def shear(self):
    wool = int(input('How much wool did you shear from {}? '.format(self.name)))
    print('The sheep is shorn, {}g of wool acquired.'.format(wool))

class Sheep(Shearing_Cattle):
  sound = 'meme'

# Птички
class Birds(Livestock):

  def collect_eggs(self):
    eggs = int(input('How many eggs did you collect from {}? '.format(self.name)))
    print('The eggs from the animal are collected, {} eggs acquired.'.format(eggs))

class Hen(Birds):
  sound = 'kokoko'
      
class Duck(Birds):
  sound = 'quack'
      
class Goose(Birds):
  sound = 'honk'

goose_seryi = Goose('Серый', 15)
goose_belyi = Goose('Белый', 18)
cow_manka = Cow('Манька', 80)
sheep_barashek = Sheep('Барашек', 35)
sheep_kudryavyi = Sheep('Кудрявый', 30)
hen_koko = Hen('Ко-Ко', 7)
hen_kukareku = Hen('Кукареку', 10)
goat_roga = Goat('Рога', 40)
goat_kopyta = Goat('Копыта', 41)
duck_kryakva = Duck('Кряква', 16)

def count_overall_weight():
  weight = 0
  for animal in gc.get_objects():
    if isinstance(animal, Livestock):
      weight += animal.weight
  print('Overall weight of all animals is {}kg.'.format(weight))

count_overall_weight()

def find_the_heaviest_animal():
  weight_list = [animal.weight for animal in gc.get_objects() if isinstance(animal, Livestock)]
  for animal in gc.get_objects():
    if isinstance(animal, Livestock):
      if animal.weight == max(animal for animal in weight_list):
        print('The heaviest animal is {}.'.format(animal.name))

find_the_heaviest_animal()
