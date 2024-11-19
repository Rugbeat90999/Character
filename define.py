from CommonLib.classes import UUID, OutputColors
import random




# Colors for console output
DEFA = str(OutputColors())
TITLE = str(OutputColors(font="bold", color="red"))
COL = str(OutputColors(color="magenta")) + ": " + str(DEFA)
CON = str(OutputColors(color="green"))
VAR = str(OutputColors(color="cyan"))
CBO = str(OutputColors(color="yellow")) + "\u007b" + str(DEFA)
CBC = str(OutputColors(color="yellow")) + "\u007d" + str(DEFA)
SBO = str(OutputColors(color="yellow")) + "[" + str(DEFA)
SBC = str(OutputColors(color="yellow")) + "]" + str(DEFA)
COM = str(OutputColors(color="red")) + ", " + str(DEFA)
ERR = str(OutputColors(color="magenta"))
CLS = str(OutputColors(color="green", font="bold"))




def registry_name_check(name:str, registry: "Items"):
  if not isinstance(registry, Items):
    raise ValueError(f"registry must be an instance of Items not {type(registry)}")
  if not isinstance(name, str):
    raise ValueError(f"name must be a string not {type(name)}")
  if name[0] == "_":
    raise ValueError(f"Name '{name}' cannot start with underscore")
  if type(name[0]) == int:
    raise ValueError(f"Name '{name}' cannot start with a number")
  if name[-1] == "_":
    raise ValueError(f"Name '{name}' cannot end with underscore")
  for part in name.split("_"):
    if not part.isalnum():
      raise ValueError(f"Name '{name}' cannot contain special characters besides underscore")
  for reg in registry.name_list():
    if reg == name:
      raise ValueError(f"Name '{name}' already exists")




class Tag:
  registerd = list["Tag"]()
  def __init__(self, tag:str, parent: "Tag" = None):
    if not isinstance(tag, str):
      raise ValueError(f"tag must be a string not {type(tag)}")
    for i in tag.split("_"):
      if not i.isalpha():
        raise ValueError("tag must only contain alphabetic characters and underscore")
    if not isinstance(parent, (Tag, type(None))):
      raise ValueError(f"parent must be a Tag not {type(parent)}")
    self.__parent = "Base"
    if parent != None:
      self.__parent = parent
    
    self.__tag = tag
    Tag.registerd.append(self)


       
  @property
  def tag(self):
    li = []
    parent = self.__parent
    while True:
      li.insert(0, parent.current_tag)
      parent = parent.parent
      if parent == "Base":
        break

    return f"{".".join(li)}.{self.__tag}" 

  
  @property
  def current_tag(self):
    return self.__tag


  @property
  def parent(self):
    return self.__parent




# Item
class Items:
  def __init__(self, weight: bool, value: bool, stack_size: bool):
    if not isinstance(weight, bool):
      raise ValueError(f"weight must be a bool not {type(weight)}")
    if not isinstance(value, bool):
      raise ValueError(f"value must be a bool not {type(value)}")
    if not isinstance(stack_size, bool):
      raise ValueError(f"stack_size must be a bool not {type(stack_size)}")
    self.weight = weight
    self.value = value
    self.stack_size = stack_size
    self.__registry = list[Item]()

  def __str__(self):
    string = ""
    for item in self.__registry:
      string += f"{item}\n"
    return f"Items:\n{string}"
  
  def __getitem__(self, key):
    if isinstance(key, int):
      return self.__registry[key]
    elif isinstance(key, str):
      for item in self.__registry:
        if item["name"] == key:
          return item
      raise ValueError(f"Name \"{key}\" does not exist")
    else:
      raise TypeError("Key must be int or str")
  
  @property
  def registry(self) -> list[str]:
    return self.__registry
  



  def add(self, name: str, display_name:str, weight: int = 0,  value: int = 0, stack_size:int = 1, description: str = "N/A", tag_list: list[str] = None):
    if not self.weight:
      weight = -1
    if not self.value:
      value = -1
    if not self.stack_size:
      stack_size = -1
    item = Item(self, name, display_name, weight,  value, stack_size, description, tag_list)
    self.__registry.append(item)
    return item


  def remove(self, name: str):
    for item in self.__registry:
      if item["name"] == name:
        self.__registry.remove(item)
        return item
    raise ValueError(f"Name '{name}' does not exist")


  def get(self, name: str):
    for item in self.__registry:
      if item["name"] == name:
        return item
    raise ValueError(f"Name '{name}' does not exist")


  def name_list(self):
    for item in self.__registry:
      yield item["name"]




class Item:
  def __init__(self, registry: Items, name: str, display_name:str, weight: int,  value: int, stack_size:int, description: str , tags: list[str]):
    registry_name_check(name, registry)
    if not isinstance(display_name, str):
      raise ValueError(f"display_name must be a string not {type(display_name)}")
    if not isinstance(weight, int):
      raise ValueError(f"weight must be an int not {type(weight)}")
    if weight < -1:
      raise ValueError("weight must be greater than or equal to -1(set to -1 to remove weight)")
    if not isinstance(value, int):
      raise ValueError(f"value must be an int not {type(value)}")
    if value < -1:
      raise ValueError("value must be greater than or equal to -1(set to -1 to remove value)")
    if not isinstance(stack_size, int):
      raise ValueError(f"stack_size must be an int not {type(stack_size)}")
    if stack_size < 0:
      raise ValueError("stack_size must be greater than or equal to 0 (set to 0 to remove stack limit)")
    if not isinstance(description, str):
      raise ValueError(f"description must be a string not {type(description)}")
    if not isinstance(tags, (list, type(None))):
      raise ValueError(f"tags must be a list or None not {type(tags)}")
    if isinstance(tags, list):
      for tag in tags:
        if not isinstance(tag, str):
          raise ValueError(f"all tags must be strings")
    

    self.__registry = registry
    self.__name = name
    self.__display_name = display_name
    self.__weight = weight
    self.__value = value
    self.__stack_size = stack_size
    self.__description = description
    self.__tags = tags


  def __str__(self) -> str:
    tags = ""
    for tag in self.__tags:
      tags += f"{COM}{VAR}{tag}{DEFA}"
    tags.lstrip(COM)
    return f"{TITLE}Item{COL}{DEFA}"\
  f"\n{CON} Name{COL} {VAR}{self.__name}{DEFA}"\
  f"\n{CON} Display Name{COL} {VAR}{self.__display_name}{DEFA}"\
  f"{f"\n{CON} Value{COL} {VAR}{self.__value}" if self.__value != -1 else ""}{DEFA}"\
  f"{f"\n{CON} Stack Size{COL} {VAR}{self.__stack_size}" if self.__stack_size != 0 else ""}{DEFA}"\
  f"{f"\n{CON} Weight{COL} {VAR}{self.__weight}" if self.__weight != -1 else ""}{DEFA}"\
  f"\n{CON} Description{COL} {VAR}{self.__description}{DEFA}"\
  f"\n{CON} Tags{COL} {VAR}{self.__description}{DEFA}"\
  
  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "name":
        return self.__name
      case "display_name":
        return self.__display_name
      case "weight":
        return self.__weight
      case "value":
        return self.__value
      case "stack_size":
        return self.__stack_size
      case "description":
        return self.__description
      case _:
        raise KeyError(f"Invalid key: {key}")

  def __setitem__(self, key, value):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "name" | 0:
        self.set_name(value)
      case "display_name" | 1:
        self.set_display_name(value)
      case "weight" | 1:
        self.set_weight(value)
      case "value" | 2:
        self.set_value(value)
      case "stack_size" | 3:
        self.set_stack_size(value)
      case "description" | 4:
        self.set_description(value)
      case _:
        raise KeyError(f"Invalid key: {key}")


  def set_name(self, new_name: str):
    registry_name_check(new_name, self.__registry)
    self.__name = new_name


  def set_display_name(self, new_name: str):
    if not isinstance(new_name, str):
      raise ValueError(f"display_name must be a string not {type(new_name)}")
    self.__display_name = new_name


  def set_value(self, new_value: int):
    if self.__value == -1:
      raise AssertionError("value cannot be set as it's diabled in this item's registry")
    if not isinstance(new_value, int):
      raise ValueError(f"value must be an int not {type(new_value)}")
    if new_value < -1:
      raise ValueError("value cannot be less than -1")
    self.__value = new_value


  def set_stack_size(self, new_stack_size: int):
    if self.__stack_size == 0:
      raise AssertionError("stack_size cannot be set as it's diabled in this item's registry")
    if not isinstance(new_stack_size, int):
      raise ValueError(f"stack_size must be an int not {type(new_stack_size)}")
    self.__stack_size = new_stack_size


  def set_weight(self, new_weight: int):
    if self.__weight == -1:
      raise AssertionError("weight cannot be set as it's diabled in this item's registry")
    if not isinstance(new_weight, int):
      raise ValueError(f"weight must be an int not {type(new_weight)}")
    self.__weight = new_weight


  def set_description(self, new_description: str):
    if not isinstance(new_description, str):
      raise ValueError(f"description must be a string not {type(new_description)}")
    self.__description = new_description
  

  def add_tag(self, tag_or_tags: str | list[str]):
    if not isinstance(tag_or_tags, (str, list)):
      raise TypeError(f"tag_or_tags must be an str or a list of str not {type(tag_or_tags)}")
    if self.__tags == None:
      self.__tags = list[str]()
    if isinstance(tag_or_tags, list):
      for tag in tag_or_tags:
        if not isinstance(tag, str):
          raise TypeError(f"tag_or_tags must be a list of str not {type(tag_or_tags)}")
        self.__tags.append(tag)
    if isinstance(tag_or_tags, str):
      self.__tags.append(tag_or_tags)
  
  def remove_tag(self, tag_or_tags: str | list[str]):
    if not isinstance(tag_or_tags, (int, list)):
      raise TypeError(f"tag_or_tags must be an int or a list of str not {type(tag_or_tags)}")
    if isinstance(tag_or_tags, list):
      for tag in tag_or_tags:
        if not isinstance(tag, str):
          raise TypeError(f"tag_or_tags must be a list of str not {type(tag_or_tags)}")
        self.__tags.remove(tag)
    if isinstance(tag_or_tags, str):
      self.__tags.remove(tag_or_tags)
    if self.__tags == []:
      self.__tags = None




class ItemInstance:
  def __init__(self, item: Item, uuid: UUID):
    if not isinstance(item, Item):
      raise ValueError(f"item must be an Item not {type(item)}")
    self.__uuid = uuid
    self.__item = item
    self.__modifiers = ItemModifiers(self)


  def __str__(self):
    return f"{TITLE}Item Instance{COL}{DEFA}"\
    f"\n {CON}UUID{COL} {VAR}{self.__uuid}{DEFA}"\
    f"\n {CON}Name{COL} {VAR}{self.__item['name']}{DEFA}"\
    f"\n {CON}Display Name{COL} {VAR}{self.__item['display_name']}{DEFA}"\
    f"{f"\n {CON}Value{COL} {VAR}{self.__item['value']}" if self.__item['value'] != -1 else ""}{DEFA}"\
    f"{f"\n {CON}Stack Size{COL} {VAR}{self.__item['stack_size']}" if self.__item['stack_size'] != 0 else ""}{DEFA}"\
    f"{f"\n {CON}Weight{COL} {VAR}{self.__item['weight']}" if self.__item['weight'] != -1 else ""}{DEFA}"\
    f"\n {CON}Description{COL} {VAR}{self.__item['description']}{DEFA}"\
    f"\n {CON}Modifiers{COL} {VAR}{self.__modifiers}{DEFA}"\

  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "uuid" | 0:
        return self.__uuid
      case "name" | 1:
        return self.__item[key]
      case "value" | 2:
        return self.__item[key]
      case "stack_size" | 3:
        return self.__item[key]
      case "weight" | 4:
        return self.__item[key]
      case "description" | 5:
        return self.__item[key]
      case "item" | 6:
        return self.__item
      case "modifiers" | 7:
        return self.__modifiers
      case _:
        raise KeyError(f"Invalid key: {key}")

  def __eq__(self, other: "ItemInstance"):
    if not isinstance(other, ItemInstance):
      return False
    return all([self.__item == other["item"], self["modifiers"] == other["modifiers"]])




class ItemModifiers:
  def __init__(self, Item: ItemInstance):
    if not isinstance(Item, ItemInstance):
      raise ValueError(f"Item must be an ItemInstance not {type(Item)}")
    self.__item = Item
    self.__display_name = None
    self.__value = None
    self.__weight = None
    self.__stack_size = None
    self.__description = None
  
  def __str__(self):
    return f"{CBO}\u007b{f"{CON}display{COL} {VAR}{self.__display_name}{COM} " if self.__display_name != None else ""}{f"{CON}value{COL} {VAR}{self.__value}{COM} " if self.__value != None else ""}\
{f"{CON}weight{COL} {VAR}{self.__weight}{COM} " if self.__weight != None else ""}\
{f"{CON}stack_size{COL} {VAR}{self.__stack_size}{COM} " if self.__stack_size != None else ""}\
{f"{CON}description{COL} {VAR}{self.__description}" if self.__description != None else ""}\
{CBC}\u007d{DEFA}"\

  
  def set_display_name(self, display_name: str):
    if not isinstance(display_name, (str, None)):
      raise ValueError(f"display_name must be a string not {type(display_name)}")
    self.__display_name = display_name
    return self


  def set_value(self, value: str):
    if not isinstance(value, (str, None)):
      raise ValueError(f"value must be a string not {type(value)}")
    self.__value = value
    return self


  def set_weight(self, weight: str):
    if not isinstance(weight, (str, None)):
      raise ValueError(f"weight must be a string not {type(weight)}")
    self.__weight = weight
    return self


  def set_stack_size(self, stack_size: str):
    if not isinstance(stack_size, (str, None)):
      raise ValueError(f"stack_size must be a string not {type(stack_size)}")
    self.__stack_size = stack_size
    return self


  def set_description(self, description: str):
    if not isinstance(description, (str, None)):
      raise ValueError(f"description must be a string not {type(description)}")
    self.__description = description
    return self




# Inventory
class Slot:
  def __init__(self, slot_num: int, slot_name: str = "N/A", tags: list[Tag] | Tag = None):
    if not isinstance(slot_num, int):
      raise ValueError(f"slot_num must be an int not {type(slot_num)}")
    if not isinstance(slot_name, str):
      raise ValueError(f"slot_name must be a string not {type(slot_name)}")
    if not isinstance(tags, (Tag, list, type(None))):
      raise ValueError(f"tags must be a either Tag or list of Tag not {type(tags)}")
    if tags == []:
      tags = None
    if isinstance(tags, list):
      for tag in tags:
        if not isinstance(tag, Tag):
          raise ValueError(f"tags must only contain {CLS}Tag{ERR} not {type(tag)}")
    self.__slot_num = slot_num
    self.__slot_name = slot_name
    self.__item = None
    self.__amount = 0
    self.__tag_list = tags

  def __str__(self):
    return f"{TITLE}slot_{self.__slot_num}{COL}"\
      f"{CBO}"\
      f"{f"{CON}slot_name{COL}{VAR}\"{self.__slot_name}\"{COM}" if self.__slot_name != "N/A" else ""}"\
      f"{f"{CON}item{COL}{VAR}{self.__item["item"]["name"]}" if self.__item != None else f"{CON}item{COL}{VAR}{self.__item}"}"\
      f"{COM}{CON}amount{COL}{VAR}{self.__amount}{DEFA}"\
      f"{f"{COM}{CON}tag_list{COL}{VAR}{self.__tag_list["name"]}{CBC}{DEFA}" if self.__tag_list != None else ""}"\
      f"{CBC}"\

  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "slot_num":
        return self.__slot_num
      case "slot_name":
        return self.__slot_name
      case "item":
        return self.__item
      case "amount":
        return self.__amount
      case "tags":
        return self.__tag_list
      case _:
        raise KeyError(f"Invalid key: {key}")
  
  def __setitem__(self, key: str | int, value: ItemInstance | str | int | None | list[str]):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid index type: {type(key)}")
    if not isinstance(value, (ItemInstance, str, int, type(None), list)):
      raise TypeError(f"value must be an ItemInstance or int not {type(value)}")
    match key:
      case "slot_num":
        raise AssertionError("Cannot change slot_num after the slot is made. Try creating a new slot and deleting the old one.")
      case "slot_name":
        if not isinstance(value, str):
          raise ValueError(f"slot_name must be a string not {type(value)}")
        self.__slot_name = value
      case "item":
        if not isinstance(value, (ItemInstance, None)):
          raise TypeError(f"value must be an ItemInstance or None for inedex \"1\" or \"item\" not {type(value)}")
        if not self.__slot_name == None:
          if not value["name"] in self.__tag_list:
            raise ValueError(f"The slot cannot contain item type {value["name"]}")
        if value == None:
          self.__amount = 0
        self.__item = value
      case "amount":
        if not isinstance(value, int):
          raise TypeError(f"value for index \"2\" or \"amount\" must be an int not {type(value)}")
        if self.__item == None:
          self.__amount = 0
          raise ValueError("Cannot change amount while there's no item in this slot")
        if value <= 0:
          raise ValueError(f"amount must be greater than 0 while there's an item in this slot")
        self.__amount = value
      case "tags":
        if not isinstance(value, (list, type(None))):
          raise TypeError(f"value must be list[str] not {type(value)}")
        if value == []:
          value = None
        if isinstance(value, list):
          for tag in value:
            if not isinstance(tag, Tag):
              raise ValueError(f"tags must only contain {CLS}Tag{ERR} not {type(tag)}")
            self.value = value
      case _:
        raise KeyError(f"Invalid key: {key}")
  
  def __delitem__(self, key: str | int):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "slot_num":
        raise AssertionError("Cannot change slot_num after the slot is made. Try creating a new slot and deleting the old one.")
      case "slot_name":
        self.__slot_name = "N/A"
      case "item":
        self.__item = None
        self.__amount = 0
      case "amount":
        if self.__item != None:
          self.__amount = 1
        else:
          raise AssertionError("Nothing to delete")
      case "tags":
        self.__tag_list = None
      case _:
        raise KeyError(f"Invalid key: {key}")


  @property
  def weight(self):
    return self.__item["weight"] * self.__amount




class Inventory:
  def __init__(self, size: int, name: str, display_name: str):
    if not isinstance(size, int):
      raise ValueError(f"size must be an int not {type(size)}")
    if size < 0:
      raise ValueError("size must be greater than or qualt to 0(set to 0 to disable size limit)")
    self.__slots = list[Slot]()
    self.__name = name
    self.__display_name = display_name

    for i in range(size):
      self.__slots.append(Slot(i))

  def __str__(self):
    string = ""
    for slot in self.__slots:
      string += f"\n {str(slot)}"
    return f"{TITLE}{self.__display_name}{COL}{DEFA}{string}{DEFA}"

  def __getitem__(self, key) -> Slot:
    if isinstance(key, int):
      for slot in self.__slots:
        if slot["slot_num"] == key:
          return slot
      raise KeyError(f"Slot {key} does not exist")
    elif isinstance(key, str):
      match key:
        case "name":
          return self.__name
        case "display_name":
          return self.__display_name
    else:
      raise TypeError(f"key must be int not {type(key)}")

  def __setitem__(self, key: str | int, value: ItemInstance | int):
    for slot in self.__slots:
      if slot[0] == key:
        if isinstance(value, int):
          slot[3] = 1
          return
        elif isinstance(value, ItemInstance):
          slot[2] = value
          return
        else:
          raise TypeError(f"value must be an ItemInstance or int not {type(value)}")
    raise ValueError(f"slot {key} does not exist")

  def __delitem__(self, key):
    if not isinstance(key, int):
      raise ValueError(f"index must be an int not {type(key)}")
    for i, slot in enumerate(self.__slots):
      if slot[1] == key:
        del self.__slots[i]
        return
    raise ValueError(f"Slot {key} does not exist")
  
  def __len__(self):
    return len(self.__slots)
  
  @property
  def weight(self):
    total_weight = 0
    for slot in self.__slots:
      if slot[1] is not None:
        total_weight += slot[1]["item"]["weight"] * slot[2]
    return total_weight


  def add_slot(self, slot_num:int):
    if not isinstance(slot_num, int):
      raise ValueError(f"slot_num must be an int not {type(slot_num)}")
    for slot in self.__slots:
      if slot[1] == slot_num:
        raise ValueError(f"Slot {slot_num} already exists")
    self.__slots.append(Slot(slot_num))


  def remove_slot(self, slot_num: int):
    if not isinstance(slot_num, int):
      raise ValueError(f"slot_num must be an int not {type(slot_num)}")
    for i, slot in enumerate(self.__slots):
      if slot[1] == slot_num:
        del self.__slots[i]
        return
    raise ValueError(f"Slot {slot_num} does not exist")




class BaseEffects:
  def __init__(self):
    self.__registry = list[BaseEffect]()
  



class BaseEffect:
  pass




class Effects:
  pass




class Effect:
  pass




class EffectInstance:
  pass




class Race:
  def __init__(self):
    self.inventoreis = []
    self.effects = []




class Character:
  def __init__(self):
    self.__registry_name = None
    # self.info = self.Info()
    self.inventory = self.Inventory()

  def __str__(self):
    return f"{self.__registry_name}"
  
  class Inventory:
    def __init__(self, inventories: list[Inventory]):
      if not isinstance(inventories, list):
        raise ValueError(f"inventories must be a list of Inventory not {type(inventories)}")
      for inventory in inventories:
        if not isinstance(inventory, Inventory):
          raise ValueError(f"inventories must be a list of Inventory, cannot contain {type(inventory)}")

      self.__inventories = inventories
    
    def __getitem__(self, key) -> Inventory:
      if isinstance(key, str):
        for inventory in self.__inventories:
          if inventory["name"] == key:
            return inventory
        raise KeyError(f"Invalid key: {key}")
      else:
        raise TypeError(f"key must be int or str not {type(key)}")

  
  class Info:
    def __init__(self, name: "Character.Info.Name", race, age: int = -1, gender: str = "random", description: str = "N/A"):
      self.name = self.Name()
      self.race = None
      self.age = 0
      self.gender = gender
      self.description = ""

    def __str__(self):
      return f"Name:"\
        f"Race:"\
        f"Age:"\
        f"Gender:"\
        f"Descriptoin:"\

    class Name:
      def __init__(self, given: str, sir: str, middle: list[str]):
        self.given = given
        self.middle = middle
        self.sir = sir
      
      @property
      def full(self):
        string = ""
        for i in self.middle:
          string += f"{i} "
        return f"{self.given} {string}{self.sir}"




