from LocalLibrary import *
from CommonLib.classes import UUID, NotUniqueUUIDError
from CommonLib.functional_classes import staticproperty, staticstr
from typing import overload

global STAT_LIST
STAT_LIST = ["xp", "stat_points", "health_points", "mana_points", "stamina_points", "health", "mana", "stamina", "strength_points", "constitution_points", "agility_points", "wisdom_points", "intelligence_points", "charisma_points"]

class Registry:
  def __init__(self, name: str):
    if not isinstance(name, str):
      raise ValueError(f"Name must be a string, not {type(name)}.")
    self.name = name


class Parts(Registry):
  def __init__(self, name: str):
    super().__init__(name)
    self.grippers = self.Grippers()
    self.bodies = self.Bodies()

  @property
  def all() -> list["Part"]:
    return Parts.Grippers.all + Parts.Bodies.all

  @property
  def registered() -> list[str]:
    return Parts.Grippers.registered + Parts.Bodies.registered

  @property
  def names() -> list[str]:
    return Parts.Grippers.names + Parts.Bodies.names


  class Bodies(Registry):
    def __init__(self):
      pass

    @property
    def all(self) -> list["BodyPart"]:
      li = list["BodyPart"]()
      for regis in self.registered:
        li.append(getattr(self, regis))
      return li

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def names(self) -> list[str]:
      li = list[str]()
      for body_part in self.all:
        li.append(body_part.name)
      return li

    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n {name}"
      return f"Body Parts:{rows}"


    def unregister(self, body_part: "BodyPart"):
      if not body_part in self.all:
        raise ValueError(f"{body_part}, is not a registered body part")

      delattr(Parts, body_part.registry_name)


  class Grippers(Registry):
    def __init__(self):
      pass
    @property
    def all(self) -> list["Gripper"]:
      li = list["Gripper"]
      for regis in self.registered:
        li.append(getattr(self, regis))
      return li

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def names(self) -> list[str]:
      li = list[str]()
      for body_part in self.all:
        li.append(body_part.name)
      return li


    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n {name}"
      return f"Grippers:{rows}"



    def unregister(self, gripper:"Gripper"):
      if not isinstance(gripper, Gripper):
        raise ValueError(f"{gripper}, is not a GripperPart instance")
      if not gripper in self.all:
        raise ValueError(f"{gripper}, is not a registered gripper part")
      delattr(self, gripper.registry_name)


  class Categories:
    @property
    def all(self) -> list["Gripper"]:
      li = list["Gripper"]()
      for regis in self.registered:
        li.append(getattr(self, regis))
      return li

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def names(self) -> list[str]:
      li = list[str]()
      for body_part in self.all:
        li.append(body_part.name)
      return li

    def unregister(self, body_part: "BodyPart"):
      if not body_part in self.all:
        raise ValueError(f"{body_part}, is not a registered body part")

      delattr(self, body_part.registry_name)


  def __format__(self, format_spec:str="default"):
    match format_spec:
      case "table":
        width = 9
        for name in self.names:
          if len(name)+2 > width:
            width = len(name) + 2
    
    
        rows = ""
        b = len(self.bodies.registered)
        g = len(self.grippers.registered)
        while b > 0 or g > 0:
          temp = "\n"
          if b > 0:
            temp += f"{self.bodies.names[b-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if g > 0:
            temp += f"{self.grippers.names[g-1]}".center(width)
          else:
            temp += "".center(width)
          
          b -= 1
          g -= 1
          rows += temp
    
        return f"All body parts:"\
          f"\n{"Bodies".ljust(width)}|{"Grippers".ljust(width)}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}"\
          f"{rows}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}"\
      
      case _:
        return self.__str__()
  

  
  @overload
  def __getitem__(self, key:int) -> "Gripper":...
  @overload
  def __getitem__(self, key:str) -> "Gripper":...

  def __getitem__(self, key) -> "Gripper":
    '''
    input a string with the parts registry name, or use an integer to find it as if this were a list
    '''
    if isinstance(key, str):
      if key in self.bodies.registered:
        return getattr(self.bodies, key)
      elif key in self.grippers.registered:
        return getattr(self.grippers, key)
      else:
        raise KeyError(f"{key} is not registred here")
    elif isinstance(key, int):
      if key < 0 or key >= len(self.all):
        raise IndexError(f"Index {key} is out of range")
      part = self.all[key]
      if part in self.bodies.registered:
        return getattr(self.bodies, part)
      elif part in self.grippers.registered:
        return getattr(self.grippers, part)
      else:
        raise KeyError(f"{key} is not registred here(There is a very big problem here, because it should exist if you've gotten to here)")
    else:
      raise TypeError("Key must be a string or an integer")


class PartCategory:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.descrition = "N/A"
    self.reg_names = list[str]()
  
  @property
  def registry_name(self):
    return self.__registry_name
  
  @property
  def body_parts(self):
    this = list[str]()
    for part_registry_name in self.reg_names:
      if isinstance(getattr(Parts.Bodies, part_registry_name), BodyPart):
        this.append(part_registry_name)
    return this
  
  @property
  def grippers(self):
    this = list[str]()
    for part_registry_name in self.reg_names:
      if isinstance(getattr(Parts.Grippers, part_registry_name), Gripper):
        this.append(part_registry_name)
    return this

  @property
  def other(self):
    this = list[str]()
    for part_registry_name in self.reg_names:
      if isinstance(getattr(Parts.Bodies, part_registry_name), BodyPart):
        continue
      elif isinstance(getattr(Parts.Grippers, part_registry_name), Gripper):
        continue
      else:
        this.append(part_registry_name)
    return this


  def __str__(self):
    return self.__format__("all")

  def __format__(self, format_spec:str="name"):
    '''
    Options:
      \"all\": returns a string of all parts
      \"description\": returns a string of the description
      \"name\": returns a string of the name(default)
    '''
    match format_spec:
      case "all":
        width = 9
        for part in self.reg_names:
          if len(part)+2 > width:
            width = len(part) + 2


        rows = ""
        n = len(self.body_parts)
        o = len(self.other)
        while n > 0 or o > 0:
          temp = "\n"
          if n > 0:
            temp += f"{self.body_parts[n-1]}".center(width)
          else:
            temp += "".center(width)
          if len(self.other) > 0:
            if o > 0:
              temp += f"{self.other[o-1]}".center(width)
            else:
              temp += "".center(width)

          n -= 1
          o -= 1
          rows += temp
        return f"All Parts:"\
          f"\n{f"Body Part".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) else ""}"\
          f"\n{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) else ""}"\
          f"{rows}"\
          f"\n{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) else ""}"\

      case "description":
        return self.description
      case _:
        return self.name



  def add_part(self, registry_name:str):
    if not registry_name in Parts.all:
      raise ValueError(f"{registry_name}, is not a registered part.")
    self.reg_names.append(registry_name)
    return self


  def remove_part(self, registry_name:str):
    try:
      self.reg_names.append(registry_name)
    except ValueError as e:
      if "list.remove(x): x not in list" == str(e):
        raise RegistryError(f"{registry_name}, is not in this category")
      raise ValueError(str(e))
    return self


  def set_name(self, name:str):
    self.name = name
    return self
  

  def set_description(self, description:str):
    self.description = description
    return self


  def register(self, registry_name):
    registry_error_check(registry_name, Parts.Categories.registered)
    self.__registry_name = registry_name
    setattr(Parts.Categories, registry_name, self)
    return self


class Part:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.item = None
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def __str__(self):
    return self.__format__()

  def __format__(self, format_spec:str="default"):
    '''
    Options:
    \n  \"default\": Return a formatted string with all properties.
    \n  \"name\": Return the name.
    \n  \"description\": Return the description.
    \n  \"registry\": Returns the registry name.
    '''
    match format_spec:
      case "name":
        return self.name
      case "description":
        return self.description
      case "registry_name":
        return self.__registry_name
      case _:
        return f"Body part:"\
              f"\n  Registry Name: {self.__registry_name}"\
              f"\n  Name: {self.name}"\
              f"\n  Description: {self.description}"\


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


  def dequip(self):
    if self.item is None:
      raise EquipmentError(f"Nothing is equipped(you can't dequip your own hands!)")
    self.item = None
    return self



class BodyPart(Part):
  def __init__(self):
    super().__init__()
    self.dextarity = False

  @property
  def registry_name(self) -> str:
    return self.__registry_name
  

  def set_dextarity_of_part(self, dextarity:int):
    if not isinstance(dextarity, int):
      raise TypeError(f"{dextarity}, should be an int not a {type(dextarity)}")
    if dextarity < 0:
      raise ValueError("Dextarity must be a positive integer.")
    self.dextarity = dextarity
    return self

  def equip(self, item: "WearableItem"):
    if not isinstance(item, WearableItem):
      raise TypeError(f"{item}, is not a wearble item")
    self.item = item
    return self

  def register(self, registry_name:str, registry:Parts):
    registry_error_check(registry_name, registry.bodies)
    self.__registry_name = registry_name
    setattr(registry.bodies, registry_name, self)
    return self


class Gripper(Part):
  def __init__(self):
    super().__init__()
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def equip(self, item: "UsableItem"):
    if not isinstance(item, UsableItem):
      raise TypeError(f"{item}, is not a UsableItem")
    self.item = item
    return self


  def register(self, registry_name:str, registry: Parts):
    registry_error_check(registry_name, registry.grippers)
    self.__registry_name = registry_name
    setattr(registry.grippers, registry_name, self)
    return self




class Items(Registry):
  '''
  All items that can be in an entity's inventory
  '''
  def __init__(self, name:str):
    super().__init__(name)
    self.wearables = self.Wearables()
    self.usables = self.Usables()
    self.generals = self.Generals()
    self.categories = self.Categories()

  @property
  def all(self):
    return self.wearables.all + self.usables.all + self.generals.all
  
  @property
  def names(self):
    return self.wearables.names + self.usables.names + self.generals.names
  
  @property
  def registered(self):
    return self.wearables.registered + self.usables.registered + self.generals.registered


  def __str__(self):
    width = 9
    for item in self.names:
      if len(item)+2 > width:
        width = len(item) + 2


    rows = ""
    w = len(self.wearables.registered)
    t = len(self.usables.registered)
    g = len(self.generals.registered)
    while w > 0 or t > 0 or g > 0:
      temp = "\n"
      if w > 0:
        temp += f"{self.wearables.names[w-1]}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if t > 0:
        temp += f"{self.usables.names[t-1]}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if g > 0:
        temp += f"{self.generals.names[g-1]}".center(width)
      else:
        temp += "".center(width)
      
      w -= 1
      t -= 1
      g -= 1
      rows += temp

    return f"All items:"\
      f"\n{"Wearables".ljust(width)}|{"Usables".ljust(width)}|{"Generals".ljust(width)}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\
      f"{rows}"\
      f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}"\




  class Wearables(Registry):
    '''
    All items that can be woren by an entity
    '''
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for usable in self.registered:
        li.append(getattr(self, usable).name)
      return li


    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\

    def unregister(self, armor: "WearableItem"):
      if not isinstance(armor, WearableItem):
        raise TypeError(f"{armor}, is not a wearable item")
      if not armor.registry_name in self.registered:
        raise ValueError(f"{armor} is not registered")
      delattr(self, armor.registry_name)



  class Usables(Registry):
    '''
    All items that have an active function
    '''
    def __init__(self):
      pass

    @staticproperty
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @staticproperty
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @staticproperty
    def names(self):
      li = list["str"]()
      for wearable in self.registered:
        li.append(getattr(self, wearable).name)
      return li
 

    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n  {name}"
      return f"Usable Items:{rows}"


    def unregister(self, item: "UsableItem"):
      if not isinstance(item, UsableItem):
        raise TypeError(f"{item}, is not a wearable item")
      if not item.registry_name in self.registered:
        raise ValueError(f"{item} is not registered")
      delattr(self, item.registry_name)



  class Generals(Registry):
    '''
    All items that have an active function
    '''
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for wearable in self.registered:
        li.append(getattr(self, wearable).name)
      return li


    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\



    def unregister(self, item: "GeneralItem"):
      if not isinstance(item, GeneralItem):
        raise TypeError(f"{item}, is not a wearable item")
      if not item.registry_name in self.registered:
        raise ValueError(f"{item} is not registered")
      delattr(self, item.registry_name)



  class Categories(Registry):
    '''
    All items that have an active function
    '''
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for wearable in self.registered:
        li.append(getattr(self, wearable).name)
      return li

    def __str__(self):
      rows = ""
      for name in self.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\


    def unregister(self, item: "ItemCategory"):
      if not isinstance(item, ItemCategory):
        raise TypeError(f"{item}, is not a wearable item")
      if not item.registry_name in self.registered:
        raise ValueError(f"{item} is not registered")
      delattr(self, item.registry_name)



class ItemCategory:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = ""
    self.descrition = ""
    self.__wearable = list[str]()
    self.__usable = list[str]()
    self.__general = list[str]()
    self.__other = list[str]()

  @property
  def registry_name(self):
    return self.__registry_name

  @property
  def wearable(self):
    return self.__wearable

  @property
  def usable(self):
    return self.__usable

  @property
  def general(self):
    return self.__general

  @property
  def other(self):
    return self.__other

  @property
  def registered(self) -> list[str]:
    return self.__wearable + self.__usable + self.__general + self.__other


  def __str__(self):
    return self.__format__("items")


  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"items\": returns a string of the items\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name\n

      does name by default
    '''
    match format_spec:
      case "items":
        width = 9
        for item in self.item_reg_names:
          if len(item) > width:
            width = len(item)
        width += 4

        rows = ""
        i = len(self.wearable)
        t = len(self.usable)
        p = len(self.general)
        o = len(self.other)
        while i > 0 or t > 0 or p > 0:
          temp = "\n"
          if i > 0:
            temp += f"{self.wearable[i-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if t > 0:
            temp += f"{self.usable[t-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if p > 0:
            temp += f"{self.general[p-1]}".center(width)
          else:
            temp += "".center(width)
          if len(self.other) > 0:
            temp += "|"
            if o > 0:
              temp += f"{self.other[o-1]}".center(width)
            else:
              temp += "".center(width)

          i -= 1
          t -= 1
          p -= 1
          o -= 1
          rows += temp
        return f"All items:"\
          f"\n{"Wearables".ljust(width)}|{"Usables".ljust(width)}|{"Generals".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) else ""}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(20)}" if len(self.other) else ""}"\
          f"{rows}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(20)}" if len(self.other) else ""}"\

      case "description":
        return self.description
      case "name":
        return self.name
      case _:
        return self.name



  def add_item(self, item:"Item"):
    if not isinstance(item, Item):
      raise RegistryError(f"{item} is not an item")
    if item.registry_name not in Items.registered:
      raise RegistryError(f"{item} is not a registered item.")

    if isinstance(item, WearableItem):
      self.__wearable.append(item.registry_name)
    elif isinstance(item, UsableItem):
      self.__usable.append(item.registry_name)
    elif isinstance(item, GeneralItem):
      self.__general.append(item.registry_name)
    else:
      self.__other.append(item.registry_name)
    
    return self

  def remove_item(self, item: "Item"):
    if not isinstance(item, Item):
      raise RegistryError(f"{item} is not an item")
    if item.registry_name not in Items.registered:
      raise RegistryError(f"{item} is not a registered item.")
    if item.registry_name not in self.registered:
      raise RegistryError(f"{item} is not in category {self.name}.")

    if isinstance(item, WearableItem):
      self.__wearable.remove(item.registry_name)
    elif isinstance(item, UsableItem):
      self.__usable.remove(item.registry_name)
    elif isinstance(item, GeneralItem):
      self.__general.remove(item.registry_name)
    else:
      self.__other.remove(item.registry_name)
    
    return self


  def set_name(self, name:str):
    self.name = name
    return self
  

  def set_description(self, description:str):
    self.description = description
    return self


  def register(self, registry_name:str, registry: Items):
    registry_error_check(registry_name, registry.categories)
    self.__registry_name = registry_name
    setattr(registry.categories, registry_name, self)


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
  
  def register(self, registry_name:str, registry):
    registry_error_check(registry_name, registry)
    self.__registry_name = registry_name
    setattr(registry, registry_name, self)



class WearableItem(Item):
  def __init__(self):
    super().__init__()
    self.__registry_name = UUID().alphabetic_version
    self.wear_type = "all"
    self.body_locations = list[bytes]()
    self.slash_rating = 0
    self.pierce_rating = 0
    self.bludgeon_rating = 0
    self.durability_type = "unbreakable"
    self.durability = 0
  
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
    if not isinstance(other, WearableItem):
      return False
    if all([self.name != other.name,
    self.description != other.description,
    self.value != other.value,
    self.weight != other.weight,
    self.wear_type != other.wear_type,
    self.body_locations != other.body_locations,
    self.slash_rating != other.slash_rating,
    self.pierce_rating != other.pierce_rating,
    self.bludgeon_rating != other.bludgeon_rating,
    self.durability_type != other.durability_type,
    self.durability != other.durability]):
      return True
    return False



  def add_wear_location(self, body_part: BodyPart) -> "WearableItem":
    if body_part not in Parts.all:
      raise ValueError(f"{body_part}, is not a registerd bodypart.")
    self.body_locations.append(body_part)
    return self


  def remove_body_location(self, body_location: bytes) -> "WearableItem":
    if not body_location in self.body_locations:
      raise ValueError(f"{body_location}, is not a body location for this wearable item.")
    self.body_locations.remove(body_location)
    return self


  def set_wear_type(self, wear_type: str) -> "WearableItem":
    '''
    Wear types:\n
    all (default)\n
    single\n
    '''
    if wear_type not in ["all", "single"]:
      raise ValueError("Invalid wear type.")
    self.wear_type = wear_type
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


  def set_durability_type(self, durability_type: str) -> "WearableItem":
    '''
    Durability types:\n
    unbreakable (default)\n
    breakable\n
    event (breaks on triger)
    '''
    if durability_type not in ["unbreakable", "breakable", "event"]:
      raise ValueError("Invalid durability type.")
    self.durability_type = durability_type
    return self


  def set_durability(self, max_durability: int) -> "WearableItem":
    if max_durability < 0:
      raise ValueError("Max durability must be a non-negative integer.")
    self.durability = max_durability
    return self


  def register(self, registry_name:str, registry:Items) -> "UsableItem":
    super().register(registry_name, registry.wearables)
    return self


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
    self.use_speed = 0
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name
  

  def __str__(self):
    return f"Usable Item:"\
           f"\n  Registry name: {self.__registry_name}"\
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


  def __eq__(self, other:"UsableItem") -> bool:
    if not isinstance(other, UsableItem):
      return False
    if all([self.name != other.name,
    self.description != other.description,
    self.value != other.value,
    self.durability_type != other.durability_type,
    self.durability != other.durability,
    self.hands_needed != other.hands_needed,
    self.slash_damage != other.slash_damage,
    self.pierce_damage != other.pierce_damage,
    self.bludgeon_damage != other.bludgeon_damage,
    self.slash_rating != other.slash_rating,
    self.pierce_rating != other.pierce_rating,
    self.bludgeon_rating != other.bludgeon_rating,
    self.use_speed != other.use_speed]):
      return True
    return False


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


  def set_grippers_needed(self, hands_needed: int):
    '''
    set how many gripper slots are taken up by this item when equipped
    '''
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
    self.use_speed = speed
    return self


  def register(self, registry_name:str, registry: Items) -> "UsableItem":
    super().register(registry_name, registry.usables)
    return self


class GeneralItem(Item):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return f"Usable Item:"\
           f"\n  Registry Name: {self.registry_name}"\
           f"\n  Name: {self.name}"\
           f"\n  Description: {self.description}"\
           f"\n  Value: {self.value}"\
           f"\n  Weight: {self.weight}"\

  def __eq__(self, other:"GeneralItem") -> bool:
    if not isinstance(other, GeneralItem):
      return False
    
    if all([self.name != other.name,
    self.description != other.description,
    self.value != other.value]):
      return True
    return False


  def register(self, registry_name:str, registry:Items) -> "UsableItem":
    super().register(registry_name, registry.generals)
    return self




class Effects(Registry):
  def __init__(self, name:str):
    super().__init__(name)
    self.instants = self.Instants()
    self.temporaries = self.Temporaries()
    self.permanents = self.Permanents()
    self.others = self.Others()
    self.catagories = self.Catagories()

  @property
  def all(self):
    return self.instants.all + self.temporaries.all + self.permanents.all + self.others.all

  @property
  def registered(self):
    return self.instants.registered + self.temporaries.registered + self.permanents.registered + self.others.registered

  @property
  def names(self):
    return self.instants.names + self.temporaries.names + self.permanents.names + self.others.names

  def __str__(self):
    return Effect.__format__()

  def __format__(self, format_spec:str="All"):
    match format_spec:
      case _:
        width = 9
        for effect in Effects.names:
          if len(effect) > width:
            width = len(effect)
        width + 2


        rows = ""
        i = len(Effects.Instants.names)
        t = len(Effects.Temporaries.names)
        p = len(Effects.Permanents.names)
        o = len(Effects.Others.names)
        while i > 0 or t > 0 or p > 0:
          temp = "\n"
          if i > 0:
            temp += f"{Effects.Instants.names[i-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if t > 0:
            temp += f"{Effects.Temporaries.names[t-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if p > 0:
            temp += f"{Effects.Permanents.names[p-1]}".center(width)
          else:
            temp += "".center(width)
          if len(Effects.Others.names) > 0:
            temp += "|"
            if o > 0:
              temp += f"{Effects.Others.names[o-1]}".center(width)
            else:
              temp += "".center(width)
            

          i -= 1
          t -= 1
          p -= 1
          o -= 1
          rows += temp

        return f"Effects:"\
             f"\n{"Instant".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(Effects.Others.names) > 0 else ""}"\
             f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(Effects.Others.names) > 0 else ""}"\
             f"{rows}"\
             f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(Effects.Others.names) > 0 else ""}"\



  class Instants(Registry):
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for usable in self.registered:
        li.append(getattr(self, usable).name)
      return li


    def __str__(self) -> str:
      rows = ""
      for effect in self.names:
        rows += f"\n  {effect}"
      return f"Instant Effects:{rows}"


  class Temporaries(Registry):
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for usable in self.registered:
        li.append(getattr(self, usable).name)
      return li


    def __str__(self) -> str:
      rows = ""
      for effect in self.names:
        rows += f"\n  {effect}"
      return f"Temporary Effects:{rows}"


  class Permanents(Registry):
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for usable in self.registered:
        li.append(getattr(self, usable).name)
      return li


    def __str__(self) -> str:
      rows = ""
      for effect in self.names:
        rows += f"\n  {effect}"
      return f"Permanent Effects:{rows}"


  class Others(Registry):
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for registered in self.registered:
        li.append(getattr(self, registered).name)
      return li


    def __str__(self) -> str:
      rows = ""
      for effect in self.names:
        rows += f"\n  {effect}"
      return f"Permanent Effects:{rows}"


  class Catagories(Registry):
    def __init__(self):
      pass

    @property
    def registered(self) -> list[str]:
      return check_attr(self.__dict__)

    @property
    def all(self):
      li = []
      for registered in self.registered:
        li.append(getattr(self, registered))
      return li
    
    @property
    def names(self):
      li = list["str"]()
      for usable in self.registered:
        li.append(getattr(self, usable).name)
      return li


    def __str__(self) -> str:
      rows = ""
      for catagories in self.all:
        rows += f"{catagories}\n"
      rows = rows.removesuffix("\n")
      return f"Effects Catagories:\n"\
           f"{rows}"



class EffectCategory:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.__instant = list[str]()
    self.__temporary = list[str]()
    self.__permanent = list[str]()
    self.__other = list[str]()
    self.name = ""
    self.descrition = ""

  @property
  def effects(self):
    return self.__instant + self.__temporary + self.__permanent + self.__other

  @property
  def registry_name(self):
    return self.__registry_name
  
  @property
  def instant(self):
    return self.__instant

  @property
  def temporary(self):
    return self.__temporary

  @property
  def permanent(self):
    return self.__permanent

  @property
  def other(self):
    return self.__other



  def __str__(self):
    return self.__format__()

  def __format__(self, format_spec:str="name"):
    '''
    Options:\n
      \"effects\": returns a string of the effects\n
      \"description\": returns a string of the description\n
      \"name\": returns a string of the name(default)\n
    '''
    match format_spec:
      case "effects":
        width = 9
        for effect in self.effects:
          if len(effect) > width:
            width = len(effect)
        width += 4

        rows = ""
        i = len(self.instant)
        t = len(self.temporary)
        p = len(self.permanent)
        o = len(self.other)
        while i > 0 or t > 0 or p > 0:
          temp = "\n"
          if i > 0:
            temp += f"{self.instant[i-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if t > 0:
            temp += f"{self.temporary[t-1]}".center(width)
          else:
            temp += "".center(width)
          temp += "|"
          if p > 0:
            temp += f"{self.permanent[p-1]}".center(width)
          else:
            temp += "".center(width)
          if len(self.other) > 0:
            temp += "|"
            if o > 0:
              temp += f"{self.other[o-1]}".center(width)
            else:
              temp += "".center(width)

          i -= 1
          t -= 1
          p -= 1
          o -= 1
          rows += temp
        return f"All items:"\
          f"\n{"Instant".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) else ""}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(20)}" if len(self.other) else ""}"\
          f"{rows}"\
          f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(20)}" if len(self.other) else ""}"\

      case "description":
        return self.description
      case _:
        return self.name



  def add_effect(self, effect:"Effect"):
    if not isinstance(effect, Effect):
      raise TypeError(f"{effect} is not an effect")
    if effect.registry_name not in Effects.registered:
      raise RegistryError(f"{effect} is not a registered effect.")
    if isinstance(effect, InstantEffect):
      self.__instant.append(effect.registry_name)
    elif isinstance(effect, TemporaryEffect):
      self.__temporary.append(effect.registry_name)
    elif isinstance(effect, PermanentEffect):
      self.__permanent.append(effect.registry_name)
    else:
      self.__other.append(effect.registry_name)
    return self


  def set_name(self, name:str):
    if not isinstance(name, str):
      raise TypeError(f"{name} is not a string")
    self.name = name
    return self
  

  def set_description(self, description:str):
    if not isinstance(description, str):
      raise TypeError(f"{description} is not a string")
    self.description = description
    return self


  def register(self, registry_name:str, registry:Effects):
    registry_error_check(registry_name, registry.catagories)
    self.__registry_name = registry_name
    setattr(registry.catagories, registry_name, self)
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
  
  def __eq__(self, other: "Effect") -> bool:
    if not isinstance(other, Effect):
      raise TypeError("Effect can only be compared to an Effect")
    if all([self.name,
    self.description,
    self.resist_req,
    self.methods]):
      return True
    return False
  

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


  def add_catagory(self, category: EffectCategory):
    if not isinstance(category, EffectCategory):
      raise TypeError("Category must be an EffectCategory instance.")
    if not category.registry_name in Effects.Catagories.registered:
      raise RegistryError(f"{category} is not a registered category.")
    category.add_effect(self)
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

  def __eq__(self, other:"InstantEffect") -> bool:
    if not isinstance(other, InstantEffect):
      raise TypeError("Can only compare InstantEffect to an InstantEffect.")

    return super().__eq__(other)



  def register(self, registry_name:str, registry: Effects):
    registry_error_check(registry_name, registry)
    self.__registry_name = registry_name
    setattr(registry.instants, registry_name, self)
    return self


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

  def __eq__(self, value):
    if not isinstance(value, TemporaryEffect):
      raise TypeError("Can only compare TemporaryEffect to a TemporaryEffect.")
    if super().__eq__(value):
      if self.duration == value.duration:
        return True
    return False



  def register(self, registry_name:str, registry: Effects):
    registry_error_check(registry_name, registry)
    self.__registry_name = registry_name
    setattr(registry.temporaries, registry_name, self)
    return self


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

  def __eq__(self, other:"PermanentEffect"):
    if not isinstance(other, PermanentEffect):
      raise TypeError("Can only compare PermanentEffect to a PermanentEffect")
    if super().__eq__(other):
      if self.release_req == other.release_req:
        return True
    return False

  def register(self, registry_name:str, registry:Effects):
    registry_error_check(registry_name, registry)
    self.__registry_name = registry_name
    setattr(registry.permanents, registry_name, self)
    return self
  

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



class Locations:
  def __init__(self):
    pass



class Actions:
  def __init__(self, name: str, description: str = "N/A"):
    if not isinstance(name, str):
      raise TypeError(f"Name must be a string, not {type(name)}")
    if not isinstance(description, str):
      raise TypeError(f"Description must be a string, not {type(description)}")
    setattr(self.__class__, name, self)

    self.name = name
    self.description = description


  @property
  def registered(self) -> list["str"]:
    return check_attr(self.__dict__)

  @property
  def all(self) -> list["Action"]:
    li = []
    for registered in self.registered:
      li.append(getattr(self, registered))
    return li

  @property
  def names(self) -> str:
    li = list[str]
    for registered in self.registered:
      li.append(getattr(self, registered).name)
    return li

  def __str__(self):
    return "add Actions string"



class ActionCategory:
  pass


class Action:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"


    self.xp = 0
    self.stat = 0
    self.health = 0
    self.mana = 0
    self.stamina = 0
    self.health = 0
    self.mana = 0
    self.stamina = 0
    self.strength = 0
    self.constitution = 0
    self.agility = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0

  @property
  def registry_name(self) -> str:
    return self.__registry_name


  def __str__(self):
    return f"Action: {self.name}. placeholder"



  def set_stat_cost(self, value:int, stat:str):
    if not isinstance(value, int):
      raise TypeError(f"Value must be an integer, not {type(value)}")
    if not isinstance(stat, str):
      raise TypeError(f"Req stat must be a string, not {type(stat)}")
    if stat not in STAT_LIST:
      raise ValueError(f"Invalid stat \"{stat}\". Stat must be one of {",".join(STAT_LIST)}")
    self.req_stat = stat
    self.req_stat_value = value
    return self



  def set_name(self, name:str):
    if not isinstance(name, str):
      raise TypeError(f"Name must be a string, not {type(name)}")
    self.name = name
    return self


  def set_description(self, description:str):
    if not isinstance(description, str):
      raise TypeError(f"Description must be a string, not {type(description)}")
    self.description = description
    return self


  def set_req_stat(self, value:int, req_stat:str):
    if not isinstance(value, int):
      raise TypeError(f"Value must be an integer, not {type(value)}")
    if not isinstance(req_stat, str):
      raise TypeError(f"Req stat must be a string, not {type(req_stat)}")
    if req_stat not in STAT_LIST:
      raise ValueError(f"Invalid stat {req_stat}. Stat must be one of {",".join(STAT_LIST)}")
    self.req_stat = req_stat
    self.req_stat_value = value
    return self


  def register(self, registry_name:str, location:Actions):
    check_attr(location.__dict__)
    if registry_name in location.registered:
      raise RegistryError(f"The registry name {registry_name} is already in use.")
    setattr(location, registry_name, self)
    return self



class Use(Action):
  def __init__(self):
    super().__init__()
    self.to_use = None
    self.use_on = None
  

  def set_to_use(self, value):
    if not isinstance(value, Item | BodyPart):
      raise TypeError(f"To use must be a string, not {type(value)}")
    self.to_use = value
    return self


  def set_use_on(self, value):
    if not isinstance(value, Item | BodyPart | "Character"): # type: ignore
      raise TypeError(f"Use on must be a string, not {type(value)}")
    self.use_on = value
    return self


  def register(self, registry_name):
    return super().register(registry_name, Action)


class Move(Action):
  def __init__(self):
    super().__init__()
    self.destination = None
    self.distance = 0
    self.resistance = 0
    self.move_type = "distance"


  def set_destination(self, destination:Locations):
    if not isinstance(destination, Locations):
      raise TypeError(f"Destination must be a Locations, not {type(destination)}")
    self.destination = destination
    return self


  def set_distance(self, distance:int):
    if not isinstance(distance, int):
      raise TypeError(f"Distance must be an integer, not {type(distance)}")
    if distance < 0:
      raise ValueError("Distance must be a non-negative integer.")
    self.distance = distance
    return self
  
  def set_resistance(self, resistance:int):
    if not isinstance(resistance, int):
      raise TypeError(f"Resistance must be an integer, not {type(resistance)}")
    if resistance < 0:
      raise ValueError("Resistance must be a non-negative integer.")
    self.resistance = resistance
    return self
  

  def set_move_type(self, move_type:str):
    '''
    Options:

    \n  \"distance\"
    \n  \"location\"
    '''
    if not isinstance(move_type, str):
      raise TypeError(f"move_type must be a string, not {type(move_type)}")
    if move_type not in ["distance", "destination"]:
      raise ValueError("Invalid move_type")
    self.move_type = move_type
    return self


  def register(self, registry_name):
    super().register(registry_name, Action)
    return self


def registry_error_check(registry_name:str, current_registry:Registry) -> None:
  if not isinstance(current_registry, Registry):
    raise TypeError("current_registry must be a Registry.")

  if not registry_name:
    raise RegistryError(f"Registry name cannot be empty.")
  
  if registry_name[0] == "_":
    raise RegistryError(f"{registry_name}, registry name cannot start with '_'.")
  
  if registry_name[0].isnumeric():
    raise RegistryError(f"{registry_name}, registry name cannot start with a number.")
  
  reg = registry_name.split("_")
  for i in reg:
    if not i.isalnum():
      raise RegistryError(f"{registry_name}, registry name cannot contain special characters.")

  for i in current_registry.registered:
      if i == registry_name:
        raise RegistryError(f"\"{registry_name}\", is not unique.")