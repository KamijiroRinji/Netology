# Сельскохозяйственные животные
class Livestock():
  legs = 0
  sound = None
  weight = 0
  
  def eat(self):
    print('nom-nom')
    
  def say(self):
    print(self.sound)
    
  def weight_gain(self, annex):
    self.weight += annex

# Скот
class Cattle(Livestock):
  legs = 4
  
  def breed(self, offspring):
    heads = int(input('Heads before:'))
    heads += offspring
    print('Heads now:', heads)
    
class Cow(Cattle):
  sound = 'moo'
  tail = None
  
  def wiggle_tail(self):
    self.tail = 'wiggle-wiggle'
  
class Goat(Cattle):
  sound = 'bee'
  angry = False
  
  def kick(self):
    if self.angry == True:
      print('Go away!')
      
class Sheep(Cattle):
  sound = 'meme'
  position = 0
  
  def travel(self, distance):
    self.position += distance
    
class Pig(Cattle):
  sound = 'oink'
  mud = 0
  
  def taking_mud_bath(self):
    while self.mud > 0:
      print('Happy piggy is taking bath :3')
      self.mud -= 1
    else:
      print('No more mud for piggy :<')

# Птички
class Birds(Livestock):
  legs = 2
  average_annual_fluff_yield = 0 
  # Сколько в среднем пуха в килограммах за год получаем с птицы
  
  def count_fluff_yield(self):
    birds = int(input('Number of birds:'))
    fluff_yield = self.average_annual_fluff_yield * birds
    print('Amount of fluff this year:', fluff_yield)

class Hen(Birds):
  sound = 'kokoko'
  golden_egg = 0
  
  def make_priest_rip_bible(self):
    if self.golden_egg > 0:
      print('Поп затужил-загоревал, свою книгу в клочья изорвал!')
    else:
      print('яичко')
      
class Duck(Birds):
  sound = 'quack'
  hungry = False
  
  def dive(self):
    food_in_water = input('Is there food in the water? Y/N').lower()
    if self.hungry == True:
      if food_in_water == 'y':
        self.eat()
      elif food_in_water == 'n':
        print('So sad T.T')
      else:
        self.say()
    else:
      print('*swam away*')
      
class Goose(Birds):
  sound = 'honk'
  danger = False
  
  def guard(self):
    while self.danger == True:
      self.say()
