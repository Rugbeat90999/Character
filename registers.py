from LocalLibrary import *
from CommonLib.classes import UUID, NotUniqueUUIDError
from CommonLib.functional_classes import staticproperty, staticstr




class BodyLocations:
  @staticproperty
  def all() -> list["Griper"]:
    li = list["Griper"]()
    for regis in BodyLocations.registered:
      li.append(getattr(BodyLocations, regis))
    return li

  @staticproperty
  def registered() -> list[str]:
    return check_attr(BodyLocations.__dict__)
  
  @staticmethod
  def unregister():
    pass


class BodyPart:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.wearing = None
  
  def set_name(self, name:str):
    if not isinstance(name, str):
      raise TypeError(f"{name}, is not a string")
    self.name = name
    return self
  

  def set_description(self, description:str):
    if not isinstance(description, str):
      raise TypeError(f"{description}, is not a string")
    self.description = description
    return self


  def grab(self, item: "UsableItem"):
    if not isinstance(item, UsableItem):
      raise TypeError(f"{item}, is not a usable item")
    self.wearing = item
    return self


  def release(self):
    self.wearing = None
    return self


  def register(self, registry_name:str):
    registry_error_check(registry_name, BodyLocations.registered)
    
    setattr(BodyLocations, registry_name, self)



class ItemLocations:
  @staticproperty
  def all() -> list["Griper"]:
    li = []
    for regis in ItemLocations.registered():
      li.append(getattr(ItemLocations, regis))
    return li

  @staticproperty
  def registered() -> list[str]:
    return check_attr(Items.Wearables.__dict__)
  
  @staticmethod
  def unregister(griper:"Griper"):
    registry_error_check(griper, ItemLocations.registered)


class Griper:
  def __init__(self, uuid:UUID):
    for i in ItemLocations.all:
      if i.uuid == self.__uuid:
        raise NotUniqueUUIDError(f"{self} does not have a unique uuid")
    self.__uuid = uuid
    self.__registry_name = uuid.alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.holding = None

  def set_name(self, name:str):
    if not isinstance(name, str):
      raise TypeError(f"{name}, is not a string")
    self.name = name
    return self
  
  def set_description(self, description:str):
    if not isinstance(description, str):
      raise TypeError(f"{description}, is not a string")
    self.description = description
    return self

  def grab(self, item: "UsableItem"):
    if not isinstance(item, UsableItem):
      raise TypeError(f"{item}, is not a usable item")
    self.holding = item


  def release(self):
    self.holding = None


  def register(self, registry_name:str):
    registry_error_check(registry_name, ItemLocations.registered)
    
    setattr(ItemLocations, registry_name, self)




class Action:
  def __init__(self):
    pass




class Items(metaclass=staticstr):
  '''
  All items that can be in an entity's inventory
  '''
  @staticproperty
  def wearables() -> list["InstantEffect"]:
    return Items.Wearables.all

  @staticproperty
  def usables():
    return Items.Usables.all

  @staticproperty
  def generals():
    return Items.Generals.all

  @staticproperty
  def items():
    return Items.wearables + Items.usables + Items.generals


  def __str__():
    width = 9
    for item in Items.items:
      if len(item.name)+2 > width:
        width = len(item.name) + 2


    rows = ""
    i = len(Items.wearables)
    t = len(Items.usables)
    p = len(Items.generals)
    while i > 0 or t > 0 or p > 0:
      temp = "\n"
      if i > 0:
        temp += f"{Items.wearables[i-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if t > 0:
        temp += f"{Items.usables[t-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if p > 0:
        temp += f"{Items.generals[p-1].name}".center(width)
      else:
        temp += "".center(width)
      
      i -= 1
      t -= 1
      p -= 1
      rows += temp

    return f"All items:"\
      f"\n{"Wearables".ljust(width)}|{"Usables".ljust(width)}|{"Generals".ljust(width)}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\
      f"{rows}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\




  class Wearables(metaclass=staticstr):
    '''
    All items that can be woren by an entity
    '''
    @staticproperty
    def registered() -> list[str]:
      return check_attr(Items.Wearables.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Items.Wearables.registered:
        li.append(getattr(Items.Wearables, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for usable in Items.Wearables.registered:
        li.append(getattr(Items.Wearables, usable).name)
      return li


    def __str__():
      rows = ""
      for name in Items.Wearables.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\

    def unregister(armor: "WearableItem"):
      if UUID_search(armor.uuid, Items.Wearables.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      delattr(Items.Wearables, armor.registry_name)



  class Usables(metaclass=staticstr):
    '''
    All items that have an active function
    '''

    @staticproperty
    def registered() -> list[str]:
      return check_attr(Items.Usables.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Items.Usables.registered:
        li.append(getattr(Items.Usables, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.Usables.registered:
        li.append(getattr(Items.Usables, wearable).name)
      return li
 

    def __str__():
      rows = ""
      for name in Items.Usables.names:
        rows += f"\n  {name}"
      return f"Usable Items:{rows}"
    

    def unregister(armor: "UsableItem"):
      if UUID_search(armor.uuid, Items.Usables.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      delattr(Items.Usables, armor.registry_name)



  class Generals(metaclass=staticstr):
    '''
    All items that have an active function
    '''

    @staticproperty
    def registered() -> list[str]:
      return check_attr(Items.Generals.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Items.Generals.registered:
        li.append(getattr(Items.Generals, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.Generals.registered:
        li.append(getattr(Items.Generals, wearable).name)
      return li

    def __str__():
      rows = ""
      for name in Items.Generals.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\


    def register(armor: "GeneralItem",):
      if UUID_search(armor.uuid, Items.Generals.all) != -1:
        raise NotUniqueUUIDError(f"The UUID of {armor} is already in use.")
      if armor.registry_name in Items.Generals.registered:
        raise RegistryError(f"The registery name {armor.registry_name} is already in use.")
      

      setattr(Items.Generals, armor.registry_name, armor)
    

    def unregister(armor: "GeneralItem"):
      if UUID_search(armor.uuid, Items.Generals.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      delattr(Items.Generals, armor.registry_name)



  class Categories(metaclass=staticstr):
    '''
    All items that have an active function
    '''

    @staticproperty
    def registered() -> list[str]:
      return check_attr(Items.Categories.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Items.Categories.registered:
        li.append(getattr(Items.Categories, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.Categories.registered:
        li.append(getattr(Items.Categories, wearable).name)
      return li

    def __str__():
      rows = ""
      for name in Items.Categories.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\



class ItemCategory:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = ""
    self.descrition = ""
    self.items = list[Item]()
  
  @property
  def registry_name(self):
    return self.__registry_name
  
  @property
  def wearable(self):
    this = list[WearableItem]()
    for effect in self.items:
      if isinstance(effect, WearableItem):
        this.append(effect)
      elif isinstance(effect, UsableItem):
        pass
      elif isinstance(effect, GeneralItem):
        pass
    return this

  @property
  def usable(self):
    this = list[UsableItem]()
    for effect in self.items:
      if isinstance(effect, WearableItem):
        pass
      elif isinstance(effect, UsableItem):
        this.append(effect)
      elif isinstance(effect, GeneralItem):
        pass
    return this

  @property
  def general(self):
    this = list[GeneralItem]()
    for effect in self.items:
      if isinstance(effect, WearableItem):
        pass
      elif isinstance(effect, UsableItem):
        pass
      elif isinstance(effect, GeneralItem):
        this.append(effect)
    return this

  @property
  def other(self):
    this = list()
    for effect in self.items:
      if isinstance(effect, WearableItem):
        pass
      elif isinstance(effect, UsableItem):
        pass
      elif isinstance(effect, GeneralItem):
        pass
      else:
        this.append(effect)
    return this



  def __str__():
    width = 9
    for item in Items.items:
      if len(item.name)+2 > width:
        width = len(item.name) + 2


    rows = ""
    i = len(Items.wearables)
    t = len(Items.usables)
    p = len(Items.generals)
    while i > 0 or t > 0 or p > 0:
      temp = "\n"
      if i > 0:
        temp += f"{Items.wearables[i-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if t > 0:
        temp += f"{Items.usables[t-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if p > 0:
        temp += f"{Items.generals[p-1].name}".center(width)
      else:
        temp += "".center(width)
      
      i -= 1
      t -= 1
      p -= 1
      rows += temp

    return f"All items:"\
      f"\n{"Wearables".ljust(width)}|{"Usables".ljust(width)}|{"Generals".ljust(width)}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\
      f"{rows}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\

  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n
      \"uuid\": returns a string of the uuid

      does name by default
    '''
    match format_spec:
      case "effects":
        return ", ".join(self.items)
      case "description":
        return self.description
      case "name":
        return self.name
      case "uuid":
        return self.uuid
      case _:
        return self.name



  def add_item(self, effect:"Item"):
    self.items.append(effect)
    return self


  def set_name(self, name:str):
    self.name = name
    return self
  

  def set_description(self, description:str):
    self.description = description
    return self


  def register(self, registry_name:str):
    registry_error_check(registry_name, Items.Categories.registered)
    self.__registry_name = registry_name
    setattr(Items.Categories, registry_name, self)


class Item:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.value = 0
    self.weight = 0
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name

  def __str__(self):
    # TODO: add this
    return "add this str"
  
  def set_name(self, name:str):
    self.name = name
    return self

  def set_description(self, description:str):
    self.description = description
    return self
  
  def set_value(self, value:int):
    if value < 0:
      raise ValueError("Value must be a non-negative integer.")
    self.value = value
    return self
  
  def set_weight(self, weight:int):
    if weight < 0:
      raise ValueError("Weight must be a non-negative integer.")
    self.weight = weight
    return self



class WearableItem(Item):
  '''
  Wearable items\n

  for setup:\n
  set_name\n
  set_description\n
  set_value\n
  set_weight\n
  add_body_location\n
  set_wear_type\n
  set_slash_rating\n
  set_pierce_rating\n
  set_bludgeon_rating\n
  set_max_durability\n
  register\n
  '''

  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
    self.body_locations = list[bytes]()
    self.wear_type = 0  
    self.slash_rating = 0
    self.pierce_rating = 0
    self.bludgeon_rating = 0
    self.durability = -1
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name

  def __str__(self):
    locations = list[str]()
    for location in self.body_locations:
      locations.append(location.decode('utf-8'))
    locations = ", ".join(locations)
    match self.wear_type:
      case 0:
        wear_type = "All"
      case 1:
        wear_type = "Single"
      case _:
        self.wear_type = 0
        wear_type = "All"
    return f"Armor Item:\n"\
           f"\nUUID: {self.__uuid}"\
           f"\nName: {self.name}"\
           f"\nDescription: {self.description}"\
           f"\nValue: {self.value}"\
           f"\nWeight: {self.weight}"\
           f"\nSlash Rating: {self.slash_rating}"\
           f"\nPierce Rating: {self.pierce_rating}"\
           f"\nBludgeon Rating: {self.bludgeon_rating}"\
           f"\nWear Type: {wear_type}"\
           f"\nWear Locations: {locations}"\
           f"{f"\nDurability: {self.durability}" if self.durability > -1 else ""}"\

  def __eq__(self, other:"WearableItem") -> bool:
    '''
    Not implemented
    '''
    raise NotImplementedError("The __eq__ method for WearableItem is not yet implemented.")

  def add_body_location(self, body_part: BodyPart) -> "WearableItem":
    if body_part not in BodyLocations.all:
      raise ValueError(f"{body_part}, is not a registerd bodypart.")
    self.body_locations.append(body_part)
    return self
  
  def remove_body_location(self, body_location: bytes) -> "WearableItem":
    if not body_location in self.body_locations:
      raise ValueError(f"{body_location}, is not a body location for this wearable item.")
    self.body_locations.remove(body_location)
    return self
  
  def set_wear_type(self, wear_type: int) -> "WearableItem":
    '''
    Wear types:\n
    default 0: all\n
    1: single\n
    '''
    match wear_type:
      case 0:
        self.wear_type = 0
      case 1:
        self.wear_type = 1
      case _:
        raise ValueError("Invalid wear type. Must be 0 (cover all) or 1 (cover single)")
    return self

  def set_slash_rating(self, slash_rating: int) -> "WearableItem":
    if slash_rating < 0:
      raise ValueError("Slash rating must be a non-negative integer.")
    self.slash_rating = slash_rating
    return self
  
  def set_pierce_rating(self, pierce_rating: int) -> "WearableItem":
    if pierce_rating < 0:
      raise ValueError("pierce rating must be a non-negative integer.")
    self.pierce_rating = pierce_rating
    return self
  
  def set_bludgeon_rating(self, bludgeon_rating: int) -> "WearableItem":
    if bludgeon_rating < 0:
      raise ValueError("Bludgeon rating must be a non-negative integer.")
    self.bludgeon_rating = bludgeon_rating
    return self
  
  def set_durability(self, max_durability: int) -> "WearableItem":
    if max_durability < 0:
      raise ValueError("Max durability must be a non-negative integer.")
    self.durability = max_durability
    return self
  
  def register(self, registry_name:str):
    registry_error_check(registry_name, Items.Wearables.registered)
    self.__registry_name = registry_name
    setattr(Items.Wearables, registry_name, self)


class UsableItem(Item):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
    self.durability_type = 0
    self.durability = 0
    self.hands_needed = 1
    self.slash_damage = 0
    self.pierce_damage = 0
    self.bludgeon_damage = 0
    self.slash_rating = 0
    self.pierce_rating = 0
    self.bludgeon_rating = 0
    self.speed = 0
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name
  
  def __str__(self):
    return f"Usable Item:"\
           f"\n  UUID: {self.__uuid}"\
           f"\n  Name: {self.name}"\
           f"\n  Description: {self.description}"\
           f"\n  Value: {self.value}"\
           f"\n  Weight: {self.weight}"\
           f"\n  Slash Damage: {self.slash_damage}"\
           f"\n  Pierce Damage: {self.pierce_damage}"\
           f"\n  Bludgeon Damage: {self.bludgeon_damage}"\
           f"\n  Slash Rating: {self.slash_rating}"\
           f"\n  Pierce Rating: {self.pierce_rating}"\
           f"\n  Bludgeon Rating: {self.bludgeon_rating}"\
           f"\n  Use Type: {self.durability_type}"\
           f"{f"\n  Durability: {self.durability}" if self.durability_type == 0 else ""}"\
  
  def set_durability_type(self, use_type:int):
    '''
    Durability type:\n
    default 0: durability\n
    default 1: event based\n
    default 2: unbreakable\n
    '''
    match use_type:
      case 0:
        self.durability_type = 0
      case 1:
        self.durability_type = 1
      case 2:
        self.durability_type = 2
      case _:
        raise ValueError(f"{use_type}, is an invalid use type.")
    return self
  
  def set_durability(self, durability:int):
    if durability < 0:
      raise ValueError("Durability must be a non-negative integer.")
    self.durability = durability
    return self
  
  def set_hands_needed(self, hands_needed: int):
    if hands_needed < 0:
      raise ValueError("Hands need must be a non-negative integer.")
    self.hands_needed = hands_needed
    return self
  
  def set_slash_damage(self, slash_damage: int):
    if slash_damage < 0:
      raise ValueError("Slash damage must be a non-negative integer.")
    self.slash_damage = slash_damage
    return self
  
  def set_pierce_damage(self, pierce_damage: int):
    if pierce_damage < 0:
      raise ValueError("Pierce damage must be a non-negative integer.")
    self.pierce_damage = pierce_damage
    return self
  
  def set_bludgeon_damage(self, bludgeon_damage: int):
    if bludgeon_damage < 0:
      raise ValueError("Bludgeon damage must be a non-negative integer.")
    self.bludgeon_damage = bludgeon_damage
    return self
  
  def set_slash_rating(self, slash_rating: int) -> "UsableItem":
    if slash_rating < 0:
      raise ValueError("Slash rating must be a non-negative integer.")
    self.slash_rating = slash_rating
    return self
  
  def set_pierce_rating(self, pierce_rating: int) -> "UsableItem":
    if pierce_rating < 0:
      raise ValueError("Pierce rating must be a non-negative integer.")
    self.pierce_rating = pierce_rating
    return self
  
  def set_bludgeon_rating(self, bludgeon_rating: int) -> "UsableItem":
    if bludgeon_rating < 0:
      raise ValueError("Bludgeon rating must be a non-negative integer.")
    self.bludgeon_rating = bludgeon_rating
    return self

  def set_speed(self, speed: int) -> "UsableItem":
    if speed < 0:
      raise ValueError("Speed must be a non-negative integer.")
    self.speed = speed
    return self

  def register(self, registry_name:str) -> "UsableItem":
    registry_error_check(registry_name, Items.Usables.registered)
    self.__registry_name = registry_name
    setattr(Items.Usables, registry_name, self)


class GeneralItem(Item):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version

  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def __str__(self):
    return f"Usable Item:"\
           f"\n  UUID: {self.__uuid}"\
           f"\n  Name: {self.name}"\
           f"\n  Description: {self.description}"\
           f"\n  Value: {self.value}"\
           f"\n  Weight: {self.weight}"\

  def register(self, registry_name:str) -> "UsableItem":
    registry_error_check(registry_name, Items.Usables.registered)
    self.__registry_name = registry_name
    setattr(Items.Usables, registry_name, self)




class Effects(metaclass=staticstr):
  @staticproperty
  def instants() -> list["InstantEffect"]:
    return Effects.Instants.all
  @staticproperty
  def temporaries():
    return Effects.Temporaries.all
  @staticproperty
  def permanents():
    return Effects.Permanents.all
  
  @staticproperty
  def effects():
    return Effects.instants + Effects.temporaries + Effects.permanents


  def __str__(self):
    width = 9
    for effect in Effects.effects:
      if len(effect.name)+2 > width:
        width = len(effect.name) + 2


    rows = ""
    i = len(Effects.instants)
    t = len(Effects.temporaries)
    p = len(Effects.permanents)
    while i > 0 or t > 0 or p > 0:
      temp = "\n"
      if i > 0:
        temp += f"{self.instants[i-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if t > 0:
        temp += f"{self.temporaries[t-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if p > 0:
        temp += f"{self.permanents[p-1].name}".center(width)
      else:
        temp += "".center(width)
      
      i -= 1
      t -= 1
      p -= 1
      rows += temp

    return f"Effects in catagory: {self.name}:"\
         f"\n{"Instant".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"{rows}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\



  class Instants(metaclass=staticstr):
    @staticproperty
    def registered() -> list[str]:
      return check_attr(Effects.Instants.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Effects.Instants.registered:
        li.append(getattr(Effects.Instants, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for usable in Effects.Instants.registered:
        li.append(getattr(Effects.Instants, usable).name)
      return li


    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Instant Effects:{rows}"


  class Temporaries(metaclass=staticstr):
    @staticproperty
    def registered() -> list[str]:
      return check_attr(Effects.Temporaries.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Effects.Temporaries.registered:
        li.append(getattr(Effects.Temporaries, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for usable in Effects.Temporaries.registered:
        li.append(getattr(Effects.Temporaries, usable).name)
      return li


    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Temporary Effects:{rows}"
  

  class Permanents(metaclass=staticstr):
    @staticproperty
    def registered() -> list[str]:
      return check_attr(Effects.Permanents.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Effects.Permanents.registered:
        li.append(getattr(Effects.Permanents, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for usable in Effects.Permanents.registered:
        li.append(getattr(Effects.Permanents, usable).name)
      return li


    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Permanent Effects:{rows}"
  

  class Catagories(metaclass=staticstr):
    @staticproperty
    def registered() -> list[str]:
      return check_attr(Effects.Catagories.__dict__)

    @staticproperty
    def all():
      li = []
      for registered in Effects.Catagories.registered:
        li.append(getattr(Effects.Catagories, registered))
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for usable in Effects.Catagories.registered:
        li.append(getattr(Effects.Catagories, usable).name)
      return li


    def __str__() -> str:
      rows = ""
      for catagories in Effects.Catagories.all:
        rows += f"{catagories}\n"
      rows = rows.removesuffix("\n")
      return f"Effects Catagories:\n"\
           f"{rows}"



class EffectCategory:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = ""
    self.descrition = ""
    self.effects = list[Item]()
  
  @property
  def registry_name(self):
    return self.__registry_name
  
  @property
  def instant(self):
    this = list[InstantEffect]()
    for effect in self.effects:
      if isinstance(effect, InstantEffect):
        this.append(effect)
      elif isinstance(effect, TemporaryEffect):
        pass
      elif isinstance(effect, PermanentEffect):
        pass
    return this

  @property
  def temporary(self):
    this = list[TemporaryEffect]()
    for effect in self.effects:
      if isinstance(effect, InstantEffect):
        pass
      elif isinstance(effect, TemporaryEffect):
        this.append(effect)
      elif isinstance(effect, PermanentEffect):
        pass
    return this

  @property
  def permanent(self):
    this = list[PermanentEffect]()
    for effect in self.effects:
      if isinstance(effect, InstantEffect):
        pass
      elif isinstance(effect, TemporaryEffect):
        pass
      elif isinstance(effect, PermanentEffect):
        this.append(effect)
    return this

  @property
  def other(self):
    this = list()
    for effect in self.effects:
      if isinstance(effect, InstantEffect):
        pass
      elif isinstance(effect, TemporaryEffect):
        pass
      elif isinstance(effect, PermanentEffect):
        pass
      else:
        this.append(effect)
    return this



  def __str__(self):
    width = 9
    for effect in self.effects:
      if len(effect.name)+2 > width:
        width = len(effect.name) + 2


    rows = ""
    i = len(self.instant)
    t = len(self.temporary)
    p = len(self.permanent)
    o = len(self.other)
    while i > 0 or t > 0 or p > 0:
      temp = "\n"
      if i > 0:
        temp += f"{self.instant[i-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if t > 0:
        temp += f"{self.temporary[t-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if p > 0:
        temp += f"{self.permanent[p-1].name}".center(width)
      else:
        temp += "".center(width)
      if len(self.other) > 0:
        if o > 0:
          temp += f"{self.other[p-1].name}".center(width)
        else:
          temp += "".center(width)
      
      i -= 1
      t -= 1
      p -= 1
      o -= 1
      rows += temp

    return f"Effects in catagory: {self.name}:"\
         f"\n{"Instant".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"{rows}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\
  

  def __format__(self, format_spec="default"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n
      \"uuid\": returns a string of the uuid

      does name by default
    '''
    match format_spec:
      case "effects":
        return ", ".join(self.effects)
      case "description":
        return self.description
      case "name":
        return self.name
      case "uuid":
        return self.uuid
      case _:
        return self.name



  def add_effect(self, effect:"Item"):
    self.effects.append(effect)
    return self


  def set_name(self, name:str):
    self.name = name
    return self
  

  def set_description(self, description:str):
    self.description = description
    return self


  def register(self, registry_name:str):
    registry_error_check(registry_name, Effects.Catagories.all)
    self.__registry_name = registry_name
    setattr(Effects.Catagories, registry_name, self)
    return self


class Effect:
  '''
This is a parent class and should not be used directly
  '''
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.resist_req = 0
    self.methods = list[tuple[str, str, int]]()
    self.catagory = list[str]()
    
    self.max_health = 0
    self.max_stamina = 0
    self.max_mana = 0
    self.health = 0
    self.stamina = 0
    self.mana = 0
    self.strength = 0
    self.constitution = 0
    self.agility = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name
  

  def set_name(self, name:str):
    if not isinstance(name, str):
      raise TypeError("Description must be a string.")
    self.name = name
    return self


  def set_description(self, description:str):
    if not isinstance(description, str):
      raise TypeError("Description must be a string.")
    self.description = description
    return self


  def add_catagory(self, category:EffectCategory):
    if not isinstance(category, EffectCategory):
      raise TypeError("Category must be an EffectCategory instance.")
    getattr(category, "add_effect")(self)
    return self
  
  def set_resist_req(self, req:int):
    if not isinstance(req, int):
      raise TypeError("Req must be an integer.")
    if req < 0:
      raise ValueError("Resist req must be a non-negative integer.")
    self.resist_req = req
    return self


  def add_minor_effect(self, *args):
    '''
Adds a new effect to the Effect based on the args given.
the first argument is the function, everything after is passed into the function

Current options for instant effects:
  damage(stat_to_damage, amount_of_damage)
  heal(stat_to_heal, amount_of_heal)

Current options for temporary effects:
  poison(stat_to_damage, amount_of_damage)
  weaken(stat_to_weaken, amount_to_weaken
  regen(stat_to_heal, amount_of_heal_per_second)
  boost(stat_to_boost, amount_to_boost)

Current options for permanent effects:
  cripple(stat_to_weaken, amount_to_weaken)
  boost(stat_to_boost, amount_of_boost)
  lycanthropey()
'''
    self.methods.append(args)
    return self


  def remove_effect(self, *args):
    '''
removes an added effect, you must put in the exact args in the exact order they were added in for it to work
    '''
    try:
      self.methods.remove(args)
    except ValueError as e:
      if str(e) == "list.remove(x): x not in list":
        raise ValueError(f"{args} is not an added effect")
      else:
        raise ValueError(e)
    return self



class InstantEffect(Effect):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name
  

  def __str__(self) -> str:
    methods = ""
    for method in self.methods:
      methods += f"{method[0]}, "
    methods = methods.removesuffix(", ")
    return f"UUID: {self.__uuid}"\
f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"
  

  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"catagories\": returns a string of the catagories\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n
      \"uuid\": returns a string of the uuid

      does name by default
    '''
    match format_spec:
      case "effects":
        return ", ".join(self.methods)
      case "catagories":
        return ", ".join(self.catagory)
      case "description":
        return self.description
      case "name":
        return self.name
      case "uuid":
        return self.uuid
      case _:
        return self.name
    

  def register(self, registry_name:str):
    registry_error_check(registry_name, Effects.Instants.registered)
    self.__registry_name = registry_name
    setattr(Effects.Instants, registry_name, self)


  def damage(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_damage, amount_to_damage

    effectable stats: "health", "stamina", "mana"
    '''
    damage_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    if amount < 1:
      raise ValueError("Instant Damage must be greater than zero.")
    damageable = ["health", "stamina", "mana"]
    if damage_type not in damageable:
      raise ValueError(f"{damage_type}, is not damageable stat, pick from: {damageable}")
    
    self.__setattr__(damage_type, self.__getattribute__(damage_type) - amount)


  def heal(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_heal, amount_to_heal

    effectable stats: "health", "stamina", "mana"
    '''
    heal_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    if amount < 1:
      raise ValueError("Instant Heal must be greater than zero.")
    healable = ["health", "stamina", "mana"]
    if heal_type not in ["health", "stamina", "mana"]:
      raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")

    self.__setattr__(heal_type, self.__getattribute__(heal_type) + amount)


  def trigger(self):
    for method in self.methods:
      self.__getattribute__(method[0])(method)


  def release(self):
    self.max_health = 0
    self.max_stamina = 0
    self.max_mana = 0
    self.health = 0
    self.stamina = 0
    self.mana = 0
    self.strength = 0
    self.constitution = 0
    self.agility = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0


class TemporaryEffect(Effect):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
    self.duration = 0.0
    self.time_passed = .0
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def __str__(self) -> str:
    methods = ""
    for method in self.methods:
      methods += f"{method[0]}, "
    methods = methods.removesuffix(", ")
    return f"UUID: {self.__uuid}"\
f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"


  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"catagories\": returns a string of the catagories\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n
      \"uuid\": returns a string of the uuid

      does name by default
    '''
    match format_spec:
      case "effects":
        return ", ".join(self.methods)
      case "catagories":
        return ", ".join(self.catagory)
      case "description":
        return self.description
      case "name":
        return self.name
      case "uuid":
        return self.uuid
      case _:
        return self.name


  def register(self, registry_name:str):
    registry_error_check(registry_name, Effects.Temporaries.registered)
    self.__registry_name = registry_name
    setattr(Effects.Temporaries, registry_name, self)


  def poison(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_poisen, amount_of_damage_per_second

    damageable_stats: "health", "stamina", "mana"
    '''
    damage_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    if amount < 1:
      raise ValueError("Amount of damage must be greater than 0.")
    damageable = ["health", "stamina", "mana"]
    if damage_type not in damageable:
      raise ValueError(f"{damage_type}, is not damageable stat, pick from: {damageable}")
    
    time_passed = self.time_passed
    if time_passed > self.duration:
      time_passed -= self.duration
    
    self.__setattr__(damage_type, self.__getattribute__(damage_type) - (amount*time_passed))
  

  def weaken(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_weaken, amount_to_weaken

    effectable stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
    '''
    damage_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    if amount < 1:
      raise ValueError("Amount of damage must be greater than 0.")
    damageable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
    if damage_type not in damageable:
      raise ValueError(f"{damage_type}, is not a stat")
    
    if self.duration > 0:
      self.__setattr__(damage_type, -amount)
    else:
      self.__setattr__(damage_type, self.__getattribute__(damage_type) + amount)


  def regen(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_heal, amount_of_heal_per_second

    damageable_stats: "health", "stamina", "mana"
    '''
    heal_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    healable = ["health", "stamina", "mana"]
    if heal_type not in healable:
      raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")

    time_passed = self.time_passed

    if time_passed > self.duration:
      time_passed -= self.duration

    self.__setattr__(heal_type, self.__getattribute__(heal_type) + (amount*time_passed))
    

  def boost(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_boost, amount_of_boost

    damageable_stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
    '''
    heal_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    healable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
    if heal_type not in healable:
      raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")
    if amount < 1:
      raise ValueError("Temporary Boost requires a positive number")
    
    if self.duration > 0:
      self.__setattr__(heal_type, amount)
    else:
      self.__setattr__(heal_type, self.__getattribute__(heal_type) - amount)
  

  def trigger(self, duration:float):
    self.duration = duration
    for method in self.methods:
      self.__getattribute__(method[0])(method)
  

  def hold(self, time_passed:float):
    self.duration -= time_passed
    self.time_passed = time_passed
    for method in self.methods:
      self.__getattribute__(method[0])(method)


  def release(self):
    self.max_health = 0
    self.max_stamina = 0
    self.max_mana = 0
    self.health = 0
    self.stamina = 0
    self.mana = 0
    self.strength = 0
    self.constitution = 0
    self.agility = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0


  def add_time(self, amount:float):
    self.duration += amount
  

  def remove_time(self, amount:float):
    self.duration -= amount


class PermanentEffect(Effect):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
    self.release_req = 0
    self.wereworlf = False
    self.end = False
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def __str__(self):
    methods = ""
    for method in self.methods:
      methods += f"{method[0]}, "
    methods = methods.removesuffix(", ")
    return f"UUID: {self.__uuid}"\
         f"{ f"\nName: {self.name}" if self.name != "" else ""}"\
         f"{ f"\nDescription: {self.description}" if self.description != "" else ""}"\
         f"{ f"\nEffects: {methods}" if methods  != [] else ""}"\
         f"{ f"\nCatagories: {self.catagory}" if self.catagory  != [] else ""}"


  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"catagories\": returns a string of the catagories\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n
      \"uuid\": returns a string of the uuid

      does name by default
    '''
    match format_spec:
      case "effects":
        return ", ".join(self.methods)
      case "catagories":
        return ", ".join(self.catagory)
      case "description":
        return self.description
      case "name":
        return self.name
      case "uuid":
        return self.uuid
      case _:
        return self.name


  def register(self, registry_name:str):
    registry_error_check(registry_name, Effects.Permanents.registered)
    self.__registry_name = registry_name
    setattr(Effects.Permanents, registry_name, self)
  

  def weaken(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_weaken, amount_to_weaken

    effectable stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
    '''
    damage_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    if amount < 1:
      raise ValueError("Amount of damage must be greater than 0.")
    damageable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
    if damage_type not in damageable:
      raise ValueError(f"{damage_type}, is not a stat")
    
    self.__setattr__(damage_type, -amount)


  def boost(self, var_tuple:tuple[str, str, int]):
    '''
    this function should not be called directly, instead use the add_effect method

    args = stat_to_boost, amount_of_boost

    damageable_stats: "max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"
    '''
    heal_type:str = var_tuple[1]
    amount:int = var_tuple[2]
    healable = ["max_health", "max_stamina", "max_mana", "strength", "constitution", "agility", "wisdom", "intelligence", "charisma"]
    if heal_type not in healable:
      raise ValueError(f"{heal_type}, is not healable stat, pick from: {healable}")
    if amount < 1:
      raise ValueError("Temporary Boost requires a positive number")
    
    self.__setattr__(heal_type, amount)
    if self.end:
      self.__setattr__(heal_type, self.__getattribute__(heal_type) + amount)
  

  def lycanthropey(self):
    '''
    this function should not be called directly, instead use the add_effect method

    no args
    '''
    self.wereworlf = True


  def trigger(self):
    for method in self.methods:
      self.__getattribute__(method[0])(method)


  def release(self, release:int):
    '''
    release = the strength of the release
    meaning the if you don't put in a strong enough release it won't work
    '''
    if self.release_req > release:
      raise ValueError("the release was not strong enough")
    self.max_health = 0
    self.max_stamina = 0
    self.max_mana = 0
    self.health = 0
    self.stamina = 0
    self.mana = 0
    self.strength = 0
    self.constitution = 0
    self.agility = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0
    self.wereworlf = False