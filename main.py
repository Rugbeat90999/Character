from registers import *
from LocalLibrary import *
from CommonLib.classes import UUID 

from registries import effect_registeries
from registries import item_registeries
from registries import body_location_registeries




class Character:
  def __init__(self):
    self.status = self.Status()
    self.spells = self.Spells()
    self.abilities = self.Abilities()
    self.skills = self.Skills()
    self.passives = self.Passives()
    self.inventory = self.Inventory()
   
   
  class Status:
    def __init__(self):
      self.effects = self.Effects()

      self.__xp = 0
      self.__stat_points = 0
      self.__health_points = 0
      self.__mana_points = 0
      self.__stamina_points = 0
      self.__health = 100
      self.__mana = 100
      self.__stamina = 100
      self.__strength_points = 0
      self.__constitution_points = 0
      self.__agility_points = 0
      self.__wisdom_points = 0
      self.__intelligence_points = 0
      self.__charisma_points = 0

    @property
    def level(self) -> int:
      level = 0
      xp = self.__xp
      while xp >= (level * 50 + 100):
        xp -= (level * 50 + 100)
        level += 1
      
      return level
    
    @property
    def xp(self) -> int:
      level = 0
      xp = self.__xp
      while xp >= (level * 50 + 100):
        xp -= (level * 50 + 100)
        level += 1
      
      return xp

    @property
    def max_health(self) -> int:
      base = 90
      points = 0
      points += self.__health_points * 5
      points += (self.level * 5)

      points += int((self.constitution * 2 + self.agility * 1.5 + self.strength) // 4 - 1)

      return base + points + self.effects.max_health

    @property
    def max_mana(self) -> int:
      base = 100
      points = 0
      points += self.__mana_points * 5
      points += (self.level * 5)
      
      return base + points

    @property
    def max_stamina(self) -> int:
      base = 100
      points = 0
      points += self.__stamina_points * 5
      points += (self.level * 5)
      
      return base + points

    @property
    def health(self) -> int:
      if self.__health > self.max_health:
        self.__health = self.max_health

      self.__health += self.effects.health

      return self.__health
     
    @property
    def mana(self) -> int:
      if self.__stamina > self.max_stamina:
        self.__stamina = self.max_stamina

      self.__mana += self.effects.mana

      return self.__stamina

    @property
    def stamina(self) -> int:
      if self.__mana > self.max_mana:
        self.__mana = self.max_mana
      
      self.__stamina += self.effects.stamina

      return self.__mana

    @property
    def strength(self) -> int:
      base = 10
      points = 0
      points += self.level + self.__strength_points
      
      return base + points

    @property
    def constitution(self) -> int:
      base = 10
      points = 0
      points += self.__constitution_points + self.level
      
      return base + points

    @property
    def agility(self) -> int:
      base = 10
      points = 0
      points += self.__agility_points + self.level
      
      return base + points

    @property
    def wisdom(self) -> int:
      base = 10
      points = 0
      points += self.__wisdom_points + self.level
      
      return base + points

    @property
    def intelligence(self) -> int:
      base = 10
      points = 0
      points += self.__intelligence_points + self.level
      
      return base + points

    @property
    def charisma(self) -> int:
      base = 10
      points = 0
      points += self.__charisma_points + self.level
      
      return base + points

    @property
    def stat_points(self) -> int:
      points = 5
      points -= (self.__health_points + self.__mana_points + self.__stamina_points + self.__strength_points + self.__constitution_points + self.__agility_points + self.__wisdom_points + self.__intelligence_points + self.__charisma_points)
      points += (self.__stat_points + self.level)

      return points


    class Effects:
      def __init__(self):
        self.instant = self.Instant()
        self.temporary = self.Temporary()
        self.permanent = self.Permanent()

      @property
      def max_health(self) -> int:
        return self.instant.max_health + self.temporary.max_health + self.permanent.max_health
      
      @property
      def max_mana(self) -> int:
        return self.instant.max_health + self.temporary.max_mana + self.permanent.max_mana
      
      @property
      def max_stamina(self) -> int:
        return self.instant.max_health + self.temporary.max_stamina + self.permanent.max_stamina
      
      @property
      def health(self) -> int:
        return self.instant.max_health + self.temporary.health + self.permanent.health
      
      @property
      def mana(self) -> int:
        return self.instant.max_health + self.temporary.mana + self.permanent.mana
      
      @property
      def stamina(self) -> int:
        return self.instant.max_health + self.temporary.stamina + self.permanent.stamina
      
      @property
      def strength(self) -> int:
        return self.instant.max_health + self.temporary.strength + self.permanent.strength
      
      @property
      def constitution(self) -> int:
        return self.instant.max_health + self.temporary.constitution + self.permanent.constitution
      
      @property
      def agility(self) -> int:
        return self.instant.max_health + self.temporary.agility + self.permanent.agility
      
      @property
      def wisdom(self) -> int:
        return self.instant.max_health + self.temporary.wisdom + self.permanent.wisdom
      
      @property
      def intelligence(self) -> int:
        return self.instant.max_health + self.temporary.intelligence + self.permanent.intelligence
      
      @property
      def charisma(self) -> int:
        return self.instant.max_health + self.temporary.charisma + self.permanent.charisma


      class Instant:
        '''
        Instant effects activate once, then dissapear.
        i.e. instant health
        '''
        def __init__(self):
          self.max_health = 0
          self.max_mana = 0
          self.max_stamina = 0
          self.health = 0
          self.mana = 0
          self.stamina = 0
          self.strength = 0
          self.constitution = 0
          self.agility = 0
          self.wisdom = 0
          self.intelligence = 0
          self.charisma = 0

          self.current = list[PermanentEffect]()
        
        def __str__(self):
          return f"max_health: {self.max_health}\n"\
          f"max_mana: {self.max_mana}\n"\
          f"max_stamina: {self.max_stamina}\n"\
          f"health: {self.health}\n"\
          f"mana: {self.mana}\n"\
          f"stamina: {self.stamina}\n"\
          f"strength: {self.strength}\n"\
          f"constitution: {self.constitution}\n"\
          f"agility: {self.agility}\n"\
          f"wisdom: {self.wisdom }\n"\
          f"intelligence: {self.intelligence}\n"\
          f"charisma: {self.charisma}"
        

        def add_effect(self, effect: PermanentEffect):
          self.current.append(effect)
        
        
        def trigger(self):
          for effect in self.current:
            effect.trigger()
            self.max_health += effect.max_health
            self.max_mana += effect.max_mana
            self.max_stamina += effect.max_stamina
            self.health += effect.health
            self.mana += effect.mana
            self.stamina += effect.stamina
            self.strength += effect.strength
            self.constitution += effect.constitution
            self.agility += effect.agility
            self.wisdom += effect.wisdom
            self.intelligence += effect.intelligence
            self.charisma += effect.charisma
        

        def release(self):
          self.max_health = 0
          self.max_mana = 0
          self.max_stamina = 0
          self.health = 0
          self.mana = 0
          self.stamina = 0
          self.strength = 0
          self.constitution = 0
          self.agility = 0
          self.wisdom = 0
          self.intelligence = 0
          self.charisma = 0
        

      class Temporary:
        '''
        Temporary effects last for a set amount of time.
        i.e. regeneration
        '''
        def __init__(self):
          self.max_health = 0
          self.max_mana = 0
          self.max_stamina = 0
          self.health = 0
          self.mana = 0
          self.stamina = 0
          self.strength = 0
          self.constitution = 0
          self.agility = 0
          self.wisdom = 0
          self.intelligence = 0
          self.charisma = 0

          self.current = list[TemporaryEffect]()
        
        def __str__(self):
          return f"max_health: {self.max_health}\n"\
          f"max_mana: {self.max_mana}\n"\
          f"max_stamina: {self.max_stamina}\n"\
          f"health: {self.health}\n"\
          f"mana: {self.mana}\n"\
          f"stamina: {self.stamina}\n"\
          f"strength: {self.strength}\n"\
          f"constitution: {self.constitution}\n"\
          f"agility: {self.agility}\n"\
          f"wisdom: {self.wisdom }\n"\
          f"intelligence: {self.intelligence}\n"\
          f"charisma: {self.charisma}"
        

        def add_effect(self, effect: TemporaryEffect):
          self.current.append(effect)
        
        
        def trigger(self, duration: int):
          for effect in self.current:
            effect.trigger(duration)
            self.max_health += effect.max_health
            self.max_mana += effect.max_mana
            self.max_stamina += effect.max_stamina
            self.health += effect.health
            self.mana += effect.mana
            self.stamina += effect.stamina
            self.strength += effect.strength
            self.constitution += effect.constitution
            self.agility += effect.agility
            self.wisdom += effect.wisdom
            self.intelligence += effect.intelligence
            self.charisma += effect.charisma
        

        def hold(self, time_passed: int):
          for effect in self.current:
            effect.hold(time_passed)
            self.max_health += effect.max_health
            self.max_mana += effect.max_mana
            self.max_stamina += effect.max_stamina
            self.health += effect.health
            self.mana += effect.mana
            self.stamina += effect.stamina
            self.strength += effect.strength
            self.constitution += effect.constitution
            self.agility += effect.agility
            self.wisdom += effect.wisdom
            self.intelligence += effect.intelligence
            self.charisma += effect.charisma
        

        def release(self):
          for effect in self.current:
            effect.release()
        

      
      class Permanent:
        '''
        Permanent effects last forever, as long as there is no outside factor to change or remove them.
        i.e. lycanthropey
        '''
        def __init__(self):
          self.max_health = 0
          self.max_mana = 0
          self.max_stamina = 0
          self.health = 0
          self.mana = 0
          self.stamina = 0
          self.strength = 0
          self.constitution = 0
          self.agility = 0
          self.wisdom = 0
          self.intelligence = 0
          self.charisma = 0

          self.current = list[PermanentEffect]()
        
        
        def __str__(self):
          return f"max_health: {self.max_health}\n"\
          f"max_mana: {self.max_mana}\n"\
          f"max_stamina: {self.max_stamina}\n"\
          f"health: {self.health}\n"\
          f"mana: {self.mana}\n"\
          f"stamina: {self.stamina}\n"\
          f"strength: {self.strength}\n"\
          f"constitution: {self.constitution}\n"\
          f"agility: {self.agility}\n"\
          f"wisdom: {self.wisdom }\n"\
          f"intelligence: {self.intelligence}\n"\
          f"charisma: {self.charisma}"
        

        def add_effect(self, effect: PermanentEffect):
          self.current.append(effect)
        
        
        def trigger(self):
          for effect in self.current:
            effect.trigger()
            self.max_health += effect.max_health
            self.max_mana += effect.max_mana
            self.max_stamina += effect.max_stamina
            self.health += effect.health
            self.mana += effect.mana
            self.stamina += effect.stamina
            self.strength += effect.strength
            self.constitution += effect.constitution
            self.agility += effect.agility
            self.wisdom += effect.wisdom
            self.intelligence += effect.intelligence
            self.charisma += effect.charisma
        

        def release(self):
          for effect in self.current:
            effect.release()


      def __str__(self):
        return f"max_health: {self.max_health}\n"\
        f"max_mana: {self.max_mana}\n"\
        f"max_stamina: {self.max_stamina}\n"\
        f"health: {self.health}\n"\
        f"mana: {self.mana}\n"\
        f"stamina: {self.stamina}\n"\
        f"strength: {self.strength}\n"\
        f"constitution: {self.constitution}\n"\
        f"agility: {self.agility}\n"\
        f"wisdom: {self.wisdom }\n"\
        f"intelligence: {self.intelligence}\n"\
        f"charisma: {self.charisma}"


      def trigger(self):
        self.instant.trigger()
        self.temporary.trigger()
        self.permanent.trigger()
      
      def hold(self):
        self.temporary.hold()
      
      def release(self):
        self.instant.release()
        self.temporary.release()
        self.permanent.release()



    def __str__(self) -> str:
      out = f'''xp: {self.xp}
level: {self.level}
max_health: {self.max_health}
max_mana: {self.max_mana}
max_stamina: {self.max_stamina}
strength: {self.strength}
constitution: {self.constitution}
agility: {self.agility}
wisdom: {self.wisdom}
intelligence: {self.intelligence}
charisma: {self.charisma}'''
      
      return out
    

    def add_xp(self, amount):
      self.__xp += amount

    def remove_xp(self, amount):
      self.__xp -= amount
      if self.xp < 0:
        self.xp = 0

    def remove_all_xp(self):
      self.__xp = 0


    def add_stat_points(self, amount:int):
      self.__stat_points += amount

    def remove_stat_points(self, amount:int):
      self.__stat_points -= amount
      if self.__stat_points < 0:
        self.__stat_points = 0

    def remove_given_stat_points(self):
      self.__stat_points = 0
    
    def upgrade_stat(self, amount:int, stat):
      if self.stat_points >= amount:
        match stat:
          case 'health':
            self.__health_points += amount
          case'mana':
            self.__mana_points += amount
          case'stamina':
            self.__stamina_points += amount
          case'strength':
            self.__strength_points += amount
          case 'constitution':
            self.__constitution_points += amount
          case 'agility':
            self.__agility_points += amount
          case 'wisdom':
            self.__wisdom_points += amount
          case 'intelligence':
            self.__intelligence_points += amount
          case 'charisma':
            self.__charisma_points += amount
          case _:
            raise ValueError(f"Invalid stat: {stat}")
      else:
        raise ValueError("Not enough stat points")

  
  class Spells:
    def __init__(self):
      pass

  
  class Abilities:
    def __init__(self):
      pass
  
  
  class Skills:
    def __init__(self):
      pass
  
  
  class Passives:
    def __init__(self):
      pass


  class Inventory:
    def __init__(self):
      self.stash = self.Stash()
      self.equipment = self.Equipment()
    
    
    class Equipment:
      '''
      Anything that can be worn or used
      '''
      def __init__(self):
        self.armor = self.Armor()
        self.weapons = self.Weapons()
        self.clothes = self.Clothes()
        self.trinkets = self.Trinkets()
        self.tools = self.Tools()

      
      class Armor:
        def __init__(self):
          self.head = None
          self.under_head = None
          self.body = None
          self.under_body = None
          self.legs = None
          self.under_legs = None
          self.feet = None
          self.under_feet = None
          self.hands = None
          self.under_hands = None
          self.stored = None

      
      class Clothes:
        def __init__(self):
          self.hat = None
          self.shirt = None
          self.bra = None
          self.pants = None
          self.underwear = None
          self.leggings = None
          self.socks = None
          self.shoes = None
          self.stored = None
        
      
      class Trinkets:
        def __init__(self):
          self.right_glove = None
          self.left_glove = None
          self.right_wrist = None
          self.left_wrist = None
          self.right_ankle = None
          self.left_ankle = None
          self.right_biscep = None
          self.left_biscep = None
          self.right_thigh = None
          self.left_thigh = None
          self.right_ear = None
          self.left_ear = None
          self.eyes = None
          self.neck = None
          self.finger1 = None
          self.finger2 = None
          self.finger3 = None
          self.finger4 = None
          self.finger5 = None
          self.finger6 = None
          self.finger7 = None
          self.finger8 = None
          self.finger9 = None
          self.finger10 = None
          self.stored = None

      
      class Weapons:
        def __init__(self):
          self.stored = []
          self.bow = None
          self.right_hip = None
          self.left_hip = None
          self.back_back = None
          self.left_back = None
          self.shield = None


      class Tools:
        def __init__(self):
          self.active = None
          self.stored = []
    
    
    class Stash:
      def __init__(self):
        self.general = list[Item]()
        self.money = self.Money()
      
      
   
      class Money:
        def __init__(self):
          self.__credit = 0
        
        @staticproperty
        def coin_types():
          return ["kings_coin", "big_platinum", "platinum", "big_silver", "big_gold", "gold", "silver", "big_copper", "copper"]
          
        @property
        def copper(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self)
          while credit >= 50:
            if credit >= 100000000000:
              credit -= 100000000000
            if credit >= 100000000:
              credit -= 100000000
            if credit >= 100000:
              credit -= 100000
            if credit >= 50:
              credit -= 50
          return credit

        @property
        def big_copper(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 50

          while credit >= 10:
            if credit >= 100000000000:
              credit -= 100000000000
            if credit >= 100000000:
              credit -= 100000000
            if credit >= 100000:
              credit -= 100000
            if credit >= 50:
              credit -= 50
            if credit >= 10:
              credit -= 10

          return credit

        @property
        def silver(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 500

          while credit >= 20:
            if credit >= 100000000000:
              credit -= 100000000000
            if credit >= 100000000:
              credit -= 100000000
            if credit >= 100000:
              credit -= 100000
            if credit >= 50:
              credit -= 50
            if credit >= 20:
              credit -= 20

          return credit

        @property
        def big_silver(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 10000
          while credit >= 20:
            credit -= 20
          return credit

        @property
        def gold(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 200000
          while credit >= 10:
            credit -= 10
          return credit

        @property
        def big_gold(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 2000000
          while credit >= 5:
            credit -= 5
          return credit

        @property
        def platinum(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 10000000
          while credit >= 10:
            credit -= 10
          return credit

        @property
        def big_platinum(self: "Character.Inventory.Stash.Money") -> int:
          credit = int(self) // 100000000
          while credit >= 1000:
            credit -= 1000
          return credit

        @property
        def kings_coin(self: "Character.Inventory.Stash.Money") -> int:
          return int(self) // 100000000000

        def __str__(self: "Character.Inventory.Stash.Money") -> str:
          output = f'''\
Copper: {self.copper}
Big Copper: {self.big_copper}
Silver: {self.silver}
Big Silver: {self.big_silver}
Gold: {self.gold}
Big Gold: {self.big_gold}
Platinum: {self.platinum}
Big Platinum: {self.big_platinum}'''
          if self.kings_coin > 0:
            output = output + f"\nKing's Coin: {self.kings_coin}"
          return output

        def __repr__(self: "Character.Inventory.Stash.Money") -> str:
          return str(int(self))

        def __format__(self, format_spec):
          '''
          Options:\n
          \"coins\": returns a string of the coins\n
          \"coin_list\": retuns a list of the coin values in decending order by the coin value\n
          \"total\": returns an int of the number of credits you have\n

          if you put anything else it will do coins by default

          '''
          if format_spec == 'coin_list':
            return [self.platinum, self.gold, self.silver, self.copper]
          elif format_spec == 'total':
            return self.__credit
          else:
            return self.__str__()

        def __int__(self: "Character.Inventory.Stash.Money") -> int:
          return int(self.__credit)

        def __eq__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) == int(other)

        def __ne__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) != int(other)

        def __lt__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) < int(other)

        def __le__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) <= int(other)

        def __mt__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) > int(other)

        def __me__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> bool:
          return int(self) >= int(other)

        def __add__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) + int(other)

        def __sub__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) - int(other)

        def __mul__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) * int(other)

        def __floordiv__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) // int(other)

        def __mod__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) % int(other)

        def __pow__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> int:
          return int(self) ** int(other)

        def __iadd__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> "Character.Inventory.Stash.Money":
          self.__credit = self + other
          return self

        def __isub__(self: "Character.Inventory.Stash.Money", other: "Character.Inventory.Stash.Money") -> "Character.Inventory.Stash.Money":
          if self.__credit < int(other):
            raise MoneyError("Target does not have enough money")
          self.__credit = self - other
          return self
        
        def add(self: "Character.Inventory.Stash.Money", amount:int, coin_type:str = "copper"):
          match coin_type:
            case "copper":
              self += amount
            case "big_copper":
              self += amount*50
            case "silver":
              self += amount*500
            case "big_silver":
              self += amount*10000
            case "gold":
              self += amount*200000
            case "big_gold":
              self += amount*2000000
            case "platinum":
              self += amount*10000000
            case "big_platinum":
              self += amount*100000000
            case "kings_coin":
              self += amount*100000000000
            case _:
              raise ValueError("invalid coin type")

        def subtract(self: "Character.Inventory.Stash.Money", amount:int, coin_type:str = "copper"):
          match coin_type:
            case "copper":
              self -= amount
            case "big_copper":
              self -= amount*50
            case "silver":
              self -= amount*500
            case "big_silver":
              self -= amount*10000
            case "gold":
              self -= amount*200000
            case "big_gold":
              self -= amount*2000000
            case "platinum":
              self -= amount*10000000
            case "big_platinum":
              self -= amount*100000000
            case "kings_coin":
              self -= amount*100000000000
            case _:
              raise ValueError("invalid coin type")

        def transfer(self: "Character.Inventory.Stash.Money", amount: int, target: "Character.Inventory.Stash.Money", coin_type:str = "copper"):
          '''
          Takes money from the target and gives it to the initiator
          '''
          target.subtract(amount, coin_type)
          self.add(amount, coin_type)
        

        
   
      class QuestItems:
        def __init__(self):
          pass
      

      class General:
        def __init__(self):
          pass
  
  
  class Info:
    '''
    This will contain all the flavor text and lore for the character
    '''
    def __init__(self):
      pass
    
    class Meta:
      '''
      This will contain info such as name, age, birth date, and birth place.
      '''
      def __init__(self):
        pass
    
    
    class Physical:
      '''
      This will contain info such as height, weight, and eye color.
      '''
      def __init__(self):
        pass





def check_attr(class_dict:dict):
  li = []
  class_dict = dict(class_dict)
  class_dict.pop('__module__')
  class_dict.pop('__dict__')
  class_dict.pop('__weakref__')
  class_dict.pop('__doc__')
  class_dict.pop('__str__')
  class_dict.pop('register')
  class_dict.pop('all')
  class_dict.pop('registered')
  class_dict.pop('names')
  class_dict.pop('uuids')
  class_dict.pop('unregister')
  for name in class_dict:
    li.append(name)
  return li

char = Character()
# print(Items.Usables.registered)
print(Items.Usables.IRON_SWORD)
UsableItem(UUID()).register("bob")
# print(Items.Usables.bob)
# print(Items.Usables.registered)