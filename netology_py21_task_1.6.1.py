# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.

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
    milk = int(input('How much milk did you milk? '))
    print('The animal is milked, {}l of milk acquired.'.format(milk))
    
class Cow(Milking_Cattle):
  sound = 'moo'
  
class Goat(Milking_Cattle):
  sound = 'bee'

# Скот для стрижки
class Shearing_Cattle(Livestock):

  def shear(self):
    wool = int(input('How much wool did you shear? '))
    print('The sheep is shorn, {}g of wool acquired.'.format(wool))

class Sheep(Shearing_Cattle):
  sound = 'meme'

# Птички
class Birds(Livestock):

  def collect_eggs(self):
    eggs = int(input('How many eggs did you collect? '))
    print('The eggs from the animal are collected, {} eggs acquired.'.format(eggs))

class Hen(Birds):
  sound = 'kokoko'
      
class Duck(Birds):
  sound = 'quack'
      
class Goose(Birds):
  sound = 'honk'
