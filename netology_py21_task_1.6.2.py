# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

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
goose_seryi.feed()
goose_seryi.collect_eggs()

goose_belyi = Goose('Белый', 18)
goose_belyi.speak()
goose_belyi.collect_eggs()

cow_manka = Cow('Манька', 80)
cow_manka.feed()
cow_manka.speak()
cow_manka.to_milk()

sheep_barashek = Sheep('Барашек', 35)
sheep_barashek.feed()
sheep_barashek.shear()

sheep_kudryavyi = Sheep('Кудрявый', 30)
sheep_kudryavyi.speak()
sheep_kudryavyi.shear()

hen_koko = Hen('Ко-Ко', 7)
hen_koko.feed()
hen_koko.collect_eggs()

hen_kukareku = Hen('Кукареку', 10)
hen_kukareku.speak()
hen_kukareku.collect_eggs()

goat_roga = Goat('Рога', 40)
goat_roga.feed()
goat_roga.to_milk()

goat_kopyta = Goat('Копыта', 41)
goat_kopyta.speak()
goat_kopyta.to_milk()

duck_kryakva = Duck('Кряква', 16)
duck_kryakva.feed()
duck_kryakva.speak()
duck_kryakva.collect_eggs()
