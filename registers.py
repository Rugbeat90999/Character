from LocalLibrary import *
from CommonLib.classes import UUID, NotUniqueUUIDError
from CommonLib.functional_classes import staticproperty, staticstr




class BodyLocation:
  NAMES = list["WearableItem"]()

  @staticmethod
  def register(name:str):
    if name in BodyLocation.NAMES:
      raise RegistryError(f"\"{name}\", is not unique.")


    BodyLocation.NAMES.append(name.encode("utf-8"))
    setattr(BodyLocation, name, (name).encode("utf-8"))


class Items(metaclass=staticstr):
  '''
  All items that can be in an entity's inventory
  '''
  def __str__():
    pass
  
  class Wearables(metaclass=staticstr):
    '''
    All items that can be woren by an entity
    '''
    all = list["WearableItem"]()

    @staticproperty
    def registered():
      li = list["str"]()
      for wearable in Items.Wearables.all:
        li.append(wearable.registry_name)
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.Wearables.all:
        li.append(wearable.name)
      return li


    def __str__():
      rows = ""
      for name in Items.Wearables.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\


    def register(armor: "WearableItem"):
      if UUID_search(armor.uuid, Items.Wearables.all) != -1:
        raise NotUniqueUUIDError(f"The UUID of {armor} is already in use.")
      if armor.registry_name in Items.Wearables.registered:
        raise RegistryError(f"The registery name {armor.registry_name} is already in use.")
      

      Items.Wearables.all.append(armor)
      setattr(Items.Wearables, armor.registry_name, armor)


    def unregister(armor: "WearableItem"):
      if UUID_search(armor.uuid, Items.Wearables.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      Items.Wearables.all.remove(armor)
      delattr(Items.Wearables, armor.registry_name)



  class Usables(metaclass=staticstr):
    '''
    All items that have an active function
    '''

    @staticproperty
    def registered():
      return check_attr(Items.Usables.__dict__)


    def __str__():
      rows = ""
      for name in Items.Usables.names:
        rows += f"\n  {name}"
      return f"Usable Items:{rows}"\


    def register(armor: "UsableItem",):
      if UUID_search(armor.uuid, Items.Usables.all) != -1:
        raise NotUniqueUUIDError(f"The UUID of {armor} is already in use.")
      if armor.registry_name in Items.Usables.registered:
        raise RegistryError(f"The registery name {armor.registry_name} is already in use.")
      

      # Items.Usables.all.append(armor)
      setattr(Items.Usables, armor.registry_name, armor)
    

    def unregister(armor: "UsableItem"):
      if UUID_search(armor.uuid, Items.Usables.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      Items.Usables.all.remove(armor)
      delattr(Items.Usables, armor.registry_name)



  class General(metaclass=staticstr):
    '''
    All items that have an active function
    '''
    all = list["GeneralItem"]()

    @staticproperty
    def registered():
      li = list["str"]()
      for wearable in Items.General.all:
        li.append(wearable.registry_name)
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.General.all:
        li.append(wearable.name)
      return li

    def __str__():
      rows = ""
      for name in Items.General.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\


    def register(armor: "GeneralItem",):
      if UUID_search(armor.uuid, Items.General.all) != -1:
        raise NotUniqueUUIDError(f"The UUID of {armor} is already in use.")
      if armor.registry_name in Items.General.registered:
        raise RegistryError(f"The registery name {armor.registry_name} is already in use.")
      

      Items.General.all.append(armor)
      setattr(Items.General, armor.registry_name, armor)
    

    def unregister(armor: "GeneralItem"):
      if UUID_search(armor.uuid, Items.General.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      Items.General.all.remove(armor)
      delattr(Items.General, armor.registry_name)



  class Categories(metaclass=staticstr):
    '''
    All items that have an active function
    '''
    all = list["ItemCategory"]()

    @staticproperty
    def registered():
      li = list["str"]()
      for wearable in Items.Categories.all:
        li.append(wearable.registry_name)
      return li
    
    @staticproperty
    def names():
      li = list["str"]()
      for wearable in Items.Categories.all:
        li.append(wearable.name)
      return li

    def __str__():
      rows = ""
      for name in Items.Categories.names:
        rows += f"\n  {name}"
      return f"Wearable Items:{rows}"\


    def register(armor: "ItemCategory",):
      if UUID_search(armor.uuid, Items.Categories.all) != -1:
        raise NotUniqueUUIDError(f"The UUID of {armor} is already in use.")
      if armor.registry_name in Items.Categories.registered:
        raise RegistryError(f"The registery name {armor.registry_name} is already in use.")
      

      Items.Categories.all.append(armor)
      setattr(Items.Categories, armor.registry_name, armor)
    

    def unregister(armor: "ItemCategory"):
      if UUID_search(armor.uuid, Items.Categories.all) == -1:
        raise ValueError(f"{armor} is not registered")
      
      Items.Categories.all.remove(armor)
      delattr(Items.Categories, armor.registry_name)
    
  


class ItemCategory:
  def __init__(self, uuid:UUID):
    self.__uuid = uuid
    self.__registry_name = uuid.alphabetic_version
    self.name = ""
    self.descrition = ""
    self.items = list[Item]()
  
  @property
  def uuid(self):
    return self.__uuid
  
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



  def __str__(self):
    width = 9
    for item in self.items:
      if len(item.name)+2 > width:
        width = len(item.name) + 2


    rows = ""
    w = len(self.wearable)
    u = len(self.usable)
    g = len(self.general)
    o = len(self.other)
    while w > 0 or u > 0 or g > 0:
      temp = "\n"
      if w > 0:
        temp += f"{self.wearable[w-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if u > 0:
        temp += f"{self.usable[u-1].name}".center(width)
      else:
        temp += "".center(width)
      temp += "|"
      if g > 0:
        temp += f"{self.general[g-1].name}".center(width)
      else:
        temp += "".center(width)
      if len(self.other) > 0:
        if o > 0:
          temp += f"{self.other[g-1].name}".center(width)
        else:
          temp += "".center(width)
      
      w -= 1
      u -= 1
      g -= 1
      rows += temp

    return f"Effects in catagory: {self.name}:"\
         f"\n{"Effects".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\
         f"{rows}"\
         f"\n{"".ljust(width)}|{"".ljust(width)}|{"".ljust(width)}{f"|{"".ljust(width)}" if len(self.other) > 0 else ""}"\
  

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


  def register(self, registrey_name:str):
    self.__registry_name = registrey_name
    Items.Categories.register(self)
    return self


class Item:
  def __init__(self, uuid:UUID):
    self.__uuid = uuid
    self.__regitry_name = uuid.alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.value = 0
    self.weight = 0
  
  @property
  def uuid(self) -> UUID:
    return self.__uuid
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name

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

  def __init__(self, uuid:UUID):
    super().__init__(uuid)
    self.__uuid = uuid
    self.__regitry_name = uuid.alphabetic_version
    self.body_locations = list[bytes]()
    self.wear_type = 0  
    self.slash_rating = 0
    self.pierce_rating = 0
    self.bludgeon_rating = 0
    self.durability = -1
  
  @property
  def uuid(self) -> UUID:
    return self.__uuid
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name

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

  def add_body_location(self, body_location: bytes) -> "WearableItem":
    if body_location not in BodyLocation.NAMES:
      raise ValueError(f"{body_location}, is not a valid body location for this wearable item.")
    self.body_locations.append(body_location)
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
  
  def register(self, registry_name) -> "WearableItem":
    self.__regitry_name = registry_name
    Items.Wearables.register(self)
    return self
  

class UsableItem(Item):
  def __init__(self, uuid: UUID):
    super().__init__(uuid)
    self.__uuid = uuid
    self.__regitry_name = uuid.alphabetic_version
    self.durability_type = 0
    self.durability = 0
    self.slash_damage = 0
    self.pierce_damage = 0
    self.bludgeon_damage = 0
    self.slash_rating = 0
    self.pierce_rating = 0
    self.bludgeon_rating = 0
  
  @property
  def uuid(self) -> UUID:
    return self.__uuid
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name
  
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
  
  def set_use_type(self, use_type:int):
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
  
  def register(self, registry_name) -> "UsableItem":
    self.__regitry_name = registry_name
    Items.Usables.register(self)
    return self


class GeneralItem(Item):
  def __init__(self):
    raise NotImplementedError("GeneralItem is not implemented")




class Action:
  def __init__(self, action_type:str, cost:int):
    section_types = ["spell", "attack"]
    if action_type not in section_types:
      raise TypeError(f"{action_type} is not a valid action type.")
    
    self.cost = cost




class Effects(metaclass=staticstr):
  @staticproperty
  def all_effects():
    return Effects.Instants.all + Effects.Temporaries.all + Effects.Permanents.all


  def __str__():
    rows = ""
    i = len(Effects.Instants.all)
    t = len(Effects.Temporaries.all)
    p = len(Effects.Permanents.all)
    while i > 0 or t > 0 or p > 0:
      temp = ""
      if i > 0:
        temp += f"{Effects.Instants.all[i-1].name}".center(20)
      else:
        temp += "          "
      temp += "|"
      if t > 0:
        temp += f"{Effects.Temporaries.all[t-1].name}".center(20)
      else:
        temp += "          "
      temp += "|"
      if p > 0:
        temp += f"{Effects.Permanents.all[p-1].name}".center(20)
      else:
        temp += "          "
      temp += "\n"
      
      i -= 1
      t -= 1
      p -= 1
      rows += temp

    return f"Effect:\n"\
         f"          |          |          \n"\
         f"{rows}"\
         f"          |          |          "


  class Instants(metaclass=staticstr):
    all = list['InstantEffect']()

    @staticproperty
    def registered() -> list[str]:
      registered = list[str]()
      for effect in Effects.Instants.all:
        registered.append(effect.registry_name)
      return registered

    @staticproperty
    def names() -> list[str]:
      names = list[str]()
      for effect in Effects.Instants.all:
        names.append(effect.name)
      return names

    
    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Instant Effects:{rows}"
    

    

    @staticmethod
    def register(effect:"InstantEffect", registrey_name:str):
      for registered_effect in Effects.Instants.all + Effects.Permanents.all + Effects.Temporaries.all:
        registered_effect.uuid.compare(effect.uuid)

      Effects.Instants.all.append(effect)
      Effects.Instants.registered.append(effect.registry_name)
      setattr(Effects.Instants, registrey_name, effect)


  class Temporaries(metaclass=staticstr):
    all = list['TemporaryEffect']()

    @staticproperty
    def registered() -> list[str]:
      registered = list[str]()
      for effect in Effects.Temporaries.all:
        registered.append(effect.registry_name)
      return registered

    @staticproperty
    def names() -> list[str]:
      names = list[str]()
      for effect in Effects.Temporaries.all:
        names.append(effect.name)
      return names

    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Temporary Effects:{rows}"


    @staticmethod
    def register(effect:"TemporaryEffect", registrey_name:str):
      for registered_effect in Effects.Instants.all + Effects.Permanents.all + Effects.Temporaries.all:
        registered_effect.uuid.compare(effect.uuid)
      Effects.Temporaries.all.append(effect)
      setattr(Effects.Temporaries, registrey_name, effect)
  

  class Permanents(metaclass=staticstr):
    all = list['PermanentEffect']()

    @staticproperty
    def registered() -> list[str]:
      registered = list[str]()
      for effect in Effects.Permanents.all:
        registered.append(effect.registry_name)
      return registered

    @staticproperty
    def names() -> list[str]:
      names = list[str]()
      for effect in Effects.Permanents.all:
        names.append(effect.name)
      return names
    

    def __str__() -> str:
      rows = ""
      for effect in Effects.Instants.all:
        rows += f"\n  {effect}"
      return f"Permanent Effects:{rows}"

    @staticmethod
    def register(effect:"TemporaryEffect", registrey_name:str):
      for registered_effect in Effects.Instants.all + Effects.Permanents.all + Effects.Temporaries.all:
        registered_effect.uuid.compare(effect.uuid)
      Effects.Permanents.all.append(effect)
      Effects.Permanents.registered.append(effect.registry_name)
      setattr(Effects.Permanents, registrey_name, effect)
  

  class Catagories(metaclass=staticstr):
    all = list['EffectCategory']()

    @staticproperty
    def registered() -> list[str]:
      registered = list[str]()
      for catagories in Effects.Catagories.all:
        registered.append(catagories.registry_name)
      return registered    

    def __str__() -> str:
      rows = ""
      for catagories in Effects.Catagories.all:
        rows += f"{catagories}\n"
      rows = rows.removesuffix("\n")
      return f"Effects Catagories:\n"\
           f"{rows}"
  
    @staticmethod
    def register(category:"EffectCategory", registrey_name:str):
      for registered_catagory in Effects.Catagories.all:
        registered_catagory.uuid.compare(category.uuid)
      Effects.Catagories.all.append(category)
      setattr(Effects.Catagories, registrey_name, category)



class EffectCategory:
  def __init__(self, uuid:UUID):
    self.__uuid = uuid
    self.__registry_name = uuid.alphabetic_version
    self.name = ""
    self.descrition = ""
    self.effects = list[Item]()
  
  @property
  def uuid(self):
    return self.__uuid
  
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
      rows += temp

    return f"Effects in catagory: {self.name}:"\
         f"\n{"Effects".ljust(width)}|{"Temporary".ljust(width)}|{"Permanent".ljust(width)}{f"|{"Other".ljust(width)}" if len(self.other) > 0 else ""}"\
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


  def register(self, registrey_name:str):
    self.__registry_name = registrey_name
    Effects.Catagories.register(self, registrey_name)
    return self


class Item:
  '''
This is a parent class and should not be used directly
  '''
  def __init__(self, uuid:UUID):
    self.__uuid = uuid
    self.name = "N/A"
    self.description = "N/A"
    self.__regitry_name = uuid.alphabetic_version
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
  def uuid(self) -> UUID:
    return self.__uuid
  

  def add_name(self, name:str):
    self.name = name
    return self


  def add_description(self, description:str):
    self.description = description
    return self


  def add_catagory(self, category:EffectCategory):
    getattr(category, "add_effect")(self)
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



class InstantEffect(Item):
  def __init__(self, uuid:UUID):
    super().__init__(uuid)
    self.__uuid = uuid
    self.__regitry_name = uuid.alphabetic_version
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name
  

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
    if registry_name in Effects.Instants.registered:
      raise ValueError(f"Duplicate registry name \"{registry_name}\"")
    self.__regitry_name = registry_name
    Effects.Instants.register(self, registry_name)


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


class TemporaryEffect(Item):
  def __init__(self, uuid:UUID):
    super().__init__(uuid)
    self.__uuid = uuid
    self.__regitry_name = uuid.alphabetic_version
    self.duration = 0.0
    self.time_passed = .0
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name


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
    if registry_name in Effects.Temporaries.registered:
      raise ValueError(f"Duplicate registry name \"{registry_name}\"")
    self.__regitry_name = registry_name
    Effects.Temporaries.register(self, registry_name)


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


class PermanentEffect(Item):
  def __init__(self, uuid:UUID):
    super().__init__(uuid)
    self.__uuid = uuid
    self.__regitry_name = uuid

    self.wereworlf = False
    self.end = False
  
  @property
  def registry_name(self) -> str:
    return self.__regitry_name


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
    if registry_name in Effects.Permanents.registered:
      raise ValueError(f"Duplicate registry name \"{registry_name}\"")
    self.__regitry_name = registry_name
    Effects.Permanents.register(self, registry_name)
  

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
    self.wereworlf = False