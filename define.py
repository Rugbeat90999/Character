from CommonLib.classes import UUID, OutputColors, Path
from CommonLib.functional_classes import staticproperty
import json




# Colors for console output
DEFA = str(OutputColors())
TITLE = str(OutputColors(font="bold", color="red"))
COL = str(OutputColors(color="magenta")) + ":" + str(DEFA)
CON = str(OutputColors(color="green"))
VAR = str(OutputColors(color="cyan"))
CBO = str(OutputColors(color="yellow")) + "\u007b" + str(DEFA)
CBC = str(OutputColors(color="yellow")) + "\u007d" + str(DEFA)
SBO = str(OutputColors(color="yellow")) + "[" + str(DEFA)
SBC = str(OutputColors(color="yellow")) + "]" + str(DEFA)
COM = str(OutputColors(color="red")) + ", " + str(DEFA)
ERR = str(OutputColors(color="magenta"))
CLS = str(OutputColors(color="green", font="bold"))

def settings() -> dict:
  with open(Path("./default_settings.cfg").path, "r", encoding="utf-8") as file:
    return json.load(file)

def lang() -> dict:
  with open(Path(f"./lang/{settings()["GENERAL"]["lang"]}.json").path, "r", encoding="utf-8") as file:
    to_parse = json.load(file)
    
    try:
      to_parse["word_direction"]
    except:
      to_parse.update({"word_direction": "right"})

    try:
      to_parse["numeral_direction"]
    except:
      to_parse.update({"numeral_direction": "right"})

    try:
      numbers = to_parse["numerals"]
      temp = {}
      for x in numbers:
        y = numbers[str(x)]
        temp.update({y: x})
      to_parse["numerals"].update(temp)
    except:
      to_parse.update({"numerals": {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}})

    return to_parse


class Parser:
  @staticmethod
  def print_lang(print_word: str) -> str:
    race_lang = lang()["race"]
    try:
      display_name = race_lang[f"{print_word}"]
      display_name.strip()
      if display_name == "":
        display_name = print_word
    except:
      display_name = print_word
    return display_name



  @staticmethod
  def number_lang(number: str) -> str:
    value = ""
    numeral_lang = lang()["numerals"]
    numeral_direction = lang()["numeral_direction"]

    for char in str(number):
      value += numeral_lang[char]


    if numeral_direction == "left":
      value_change_list = []
      for char in value:
        value_change_list.insert(0, char)
      value = "".join(value_change_list)

    return value


  @staticmethod
  def lang_number(number: str) -> str:
    value = ""
    numeral_lang = lang()["numerals"]
    numeral_direction = lang()["numeral_direction"]

    for char in str(number):
      value += numeral_lang[char]


    if numeral_direction == "left":
      value_change_list = []
      for char in value:
        value_change_list.insert(0, char)
      value = "".join(value_change_list)

    return value


  @staticmethod
  def item_lang(registry_name: str) -> tuple[str, str]:
      item_lang = lang()["item"]

      try:
        display_name = item_lang[f"{registry_name}.display_name"]
        display_name.strip()
        if display_name == "":
          display_name = registry_name
      except:
        display_name = registry_name


      try:
        description = item_lang[f"{registry_name}.description"]
        description.strip()
        if description == "":
          description = lang()["N/A"]
      except:
        description = lang()["N/A"]

      return (display_name, description)


  @staticproperty
  def NA():
    return lang()["N/A"]


  @staticmethod
  def Tags(tag_list: list[str]) -> str:
    tag_str = ""
    for tag in tag_list:
      tag_str += f"{VAR}{tag}{DEFA}{COM}"
    tag_str = tag_str.rstrip(COM)

    if tag_list == "":
      tag_list = Parser.NA

    return tag_str


  @staticmethod
  def race_lang(registry_name: str):
    race_lang = lang()["race"]
    try:
      display_name = race_lang[f"{registry_name}.display_name"]
      display_name.strip()
      if display_name == "":
        display_name = registry_name
    except:
      display_name = registry_name
    return display_name


  @staticmethod
  def inventory_lang(registry_name: str):
    race_lang = lang()["inventory"]
    try:
      display_name = race_lang[f"{registry_name}.display_name"]
      display_name.strip()
      if display_name == "":
        display_name = registry_name
    except:
      display_name = registry_name
    return display_name


  @staticmethod
  def slot_lang(slot_name: str):
    race_lang = lang()["slot"]
    try:
      display_name = race_lang[f"{slot_name}.display_name"]
      display_name.strip()
      if display_name == "":
        display_name = slot_name
    except:
      display_name = slot_name
    return display_name




class Registry:
  def __init__(self):
    self.__registry = list()

  @property
  def registry(self):
    return self.__registry
  
  @property
  def names(self):
    return [registry_item["name"] for registry_item in self.__registry]


  def get(self, name: str):
    for item in self.__registry:
      if item["registry_name"] == name:
        return item
    raise ValueError(f"registry item \"{name}\" does not exist")


  def remove(self, name: str):
    self.__registry.remove(self.get(name))


  def register(self, item:"Item"):
    if not isinstance(item.registry_name, str):
      raise ValueError(f"name must be a string not {type(item.registry_name)}")
    if item.registry_name[0] == "_":
      raise ValueError(f"Name '{item.registry_name}' cannot start with underscore")
    if type(item.registry_name[0]) == int:
      raise ValueError(f"Name '{item.registry_name}' cannot start with a number")
    if item.registry_name[-1] == "_":
      raise ValueError(f"Name '{item.registry_name}' cannot end with underscore")
    for part in item.registry_name.split("_"):
      if not part.isalnum():
        raise ValueError(f"Name '{item.registry_name}' cannot contain special characters besides underscore")
    if item.registry_name in self.names:
      raise ValueError(f"Name '{item.registry_name}' already exists")





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

  def __str__(self):
    return f"{self.__tag}"
       
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
class Item:
  registry = Registry()
  def __init__(self, registry_name: str):
    self.__registry_name = registry_name
    self.__weight = 0
    self.__value = 0
    self.__stack_size = 1
    self.__tags = []
  
  @property
  def registry_name(self) -> str:
    return self.__registry_name

  def __str__(self) -> str:
    print_lang = lang()["prints"]
    word_direction = lang()["word_direction"]

    value = Parser.number_lang(self.__value)
    stack_size = Parser.number_lang(self.__stack_size)
    weight = Parser.number_lang(self.__weight)

    display_name, description = Parser.item_lang(self.__registry_name)

    tags = Parser.Tags(self.__tags)



    right = f"{TITLE}{print_lang["item"]}{COL} {DEFA}"\
  f"\n{CON} {print_lang["registry_name"]}{COL} {VAR}{self.registry_name}{DEFA}"\
  f"\n{CON} {print_lang["display_name"]}{COL} {VAR}{display_name}{DEFA}"\
  f"{f"\n{CON} {print_lang["value"]}{COL} {VAR}{value}" if self.__value != -1 else ""}{DEFA}"\
  f"{f"\n{CON} {print_lang["stack_size"]}{COL} {VAR}{stack_size}" if self.__stack_size != 0 else ""}{DEFA}"\
  f"{f"\n{CON} {print_lang["weight"]}{COL} {VAR}{weight}" if self.__weight != -1 else ""}{DEFA}"\
  f"\n{CON} {print_lang["description"]}{COL} {VAR}{description}{DEFA}"\
  f"\n{CON} {print_lang["tags"]}{COL} {VAR}{tags}{DEFA}"\

    left = f"{COL}{TITLE}{print_lang["item"]}{DEFA}"\
  f"\n{VAR}{self.registry_name}{COL}{CON}{print_lang["registry_name"]}{DEFA}"\
  f"\n{VAR}{display_name}{COL}{CON}{print_lang["display_name"]}{DEFA}"\
  f"{f"\n{VAR}{value}{COL}{CON}{print_lang["value"]}" if self.__value != -1 else ""}{DEFA}"\
  f"{f"\n{VAR}{stack_size}{COL}{CON}{print_lang["stack_size"]}" if self.__stack_size != 0 else ""}{DEFA}"\
  f"{f"\n{VAR}{weight}{COL}{CON}{print_lang["weight"]}" if self.__weight != -1 else ""}{DEFA}"\
  f"\n{VAR}{description}{COL}{CON}{print_lang["description"]}{DEFA}"\
  f"\n{VAR}{tags}{COL}{CON}{print_lang["tags"]}{DEFA}"\

    return left if word_direction == "left" else right
  
  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "registry_name":
        return self.__registry_name
      case "display_name":
        return Parser.item_lang(self.__description)[0]
      case "weight":
        return Parser.number_lang(self.__weight)
      case "value":
        return Parser.number_lang(self.__value)
      case "stack_size":
        return Parser.number_lang(self.__stack_size)
      case "description":
        return Parser.item_lang(self.__description)[1]
      case _:
        raise KeyError(f"Invalid key: {key}")

  def __setitem__(self, key, value):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "registry_name":
        raise AssertionError("Cannot set registry name outside of definition of item")
      case "display_name":
        raise AssertionError("Cannot set display name outside of lang file")
      case "weight":
        self.set_weight(value)
      case "value":
        self.set_value(value)
      case "stack_size":
        self.set_stack_size(value)
      case "description":
        self.set_description(value)
      case _:
        raise KeyError(f"Invalid key: {key}")


  def set_value(self, new_value: int):
    if self.__value == -1:
      raise AssertionError("value cannot be set as it's diabled in this item's registry")
    if not isinstance(new_value, int):
      try:
        new_weight = Parser.lang_number(new_weight)
      except:
        raise ValueError(f"value must be an int not {type(new_value)}")
    if new_value < -1:
      raise ValueError("value cannot be less than -1")
    self.__value = new_value
    return self


  def set_stack_size(self, new_stack_size: int):
    if self.__stack_size == 0:
      raise AssertionError("stack_size cannot be set as it's diabled in this item's registry")
    if not isinstance(new_stack_size, int):
      try:
        new_weight = Parser.lang_number(new_weight)
      except:
        raise ValueError(f"stack_size must be an int not {type(new_stack_size)}")
    self.__stack_size = new_stack_size
    return self


  def set_weight(self, new_weight: int):
    if self.__weight == -1:
      raise AssertionError("weight cannot be set as it's diabled in this item's registry")

    if not isinstance(new_weight, int):
      try:
        new_weight = Parser.lang_number(new_weight)
      except:
        raise ValueError(f"weight must be an int not {type(new_weight)}")

    self.__weight = new_weight
    return self


  def set_description(self, new_description: str):
    if not isinstance(new_description, str):
      raise ValueError(f"description must be a string not {type(new_description)}")
    self.__description = new_description
    return self
  

  def add_tag(self, tag_or_tags: Tag | list[Tag]):
    if not isinstance(tag_or_tags, (Tag, list)):
      raise TypeError(f"tag_or_tags must be an str or a list of str not {type(tag_or_tags)}")
    if self.__tags == None:
      self.__tags = list[str]()
    if isinstance(tag_or_tags, list):
      for tag in tag_or_tags:
        if not isinstance(tag, Tag):
          raise TypeError(f"tag_or_tags must be a list of Tag not {type(tag_or_tags)}")
        self.__tags.append(tag)
    if isinstance(tag_or_tags, Tag):
      self.__tags.append(tag_or_tags)
    return self


  def remove_tag(self, tag_or_tags: Tag | list[Tag]):
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
    return self


  def register(self):
    Item.registry.register(self)
    return self




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
      case "display_name":
        return Parser.slot_lang(self.__slot_name)
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
  registry = Registry()
  def __init__(self, size: int, registry_name: str):
    if not isinstance(size, int):
      raise ValueError(f"size must be an int not {type(size)}")
    if size < 0:
      raise ValueError("size must be greater than or qualt to 0(set to 0 to disable size limit)")
    self.__slots = list[Slot]()
    self.__registry_name = registry_name

    for i in range(size):
      self.__slots.append(Slot(i))

  def __str__(self):
    string = ""
    for slot in self.__slots:
      string += f"\n {str(slot)}"

    return f"{TITLE}{self["display_name"]}{COL}{DEFA}{string}{DEFA}"

  def __getitem__(self, key) -> Slot:
    if isinstance(key, int):
      for slot in self.__slots:
        if slot["slot_num"] == key:
          return slot
      raise KeyError(f"Slot {key} does not exist")
    elif isinstance(key, str):
      match key:
        case "name":
          return self.__registry_name
        case "display_name":
          return Parser.inventory_lang(self.__registry_name)
    else:
      raise TypeError(f"key must be int not {type(key)}")

  def __setitem__(self, key: str | int, value: ItemInstance | int):
    for slot in self.__slots:
      if slot["slot_num"] == key:
        if isinstance(value, int):
          slot["item"] = 1
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
      if slot["slot_num"] == slot_num:
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


  def copy(self, new_name):
    inv  = Inventory(len(self.__slots), new_name)
    
    for i in range(len(self.__slots)):
      inv.__slots[i] = self.__slots[i]
    
    return inv


  def register(self):
    Inventory.registry.register(self)




class Effect:
  registry = Registry()
  def __init__(self, registry_name: str):
    self.__registry_name = registry_name
    self.__funcitons = []

  @property
  def registry_name(self):
    return self.__registry_name
  
  def funcitons_list(self):
    return self.__funcitons
  

  def activate(self):
    for func in self.__funcitons:
      return func()


  def add_func(self, func):
    if not callable(func):
      raise TypeError(f"func must be a callable not {type(func)}")
    

  def register(self):
    Effect.registry.register(self)




class EffectInstance:
  pass




class Race:
  registry = Registry()
  def __init__(self, registry_name: str, inventories: list[Inventory], race_effects: list[Effect]):
    self.__registry_name = registry_name
    self.inventories = inventories
    self.effects = race_effects

  def __str__(self):
    inventories = ""
    for inventory in self.inventories:
      inventories += f"{VAR}{inventory["display_name"]}{COM}"
    inventories = inventories.rstrip(f"{COM}")

    effects = None
    # for effect in self.inventories:
      # effects += f"{VAR}{effect["display_name"]}{COM}"
    # effects = effects.rstrip(f"{COM}")

    left = f"{TITLE}Race{COL}{DEFA}"\
    f"\n {CON}{lang()["prints"]["registry_name"]}{COL}{VAR}{self.__registry_name}{DEFA}"\
    f"\n {CON}{lang()["prints"]["display_name"]}{COL}{VAR}{self["display_name"]}{DEFA}"\
    f"\n {CON}{lang()["prints"]["inventories"]}{COL}{inventories}{DEFA}"\
    f"\n {CON}{lang()["prints"]["effects"]}{COL}{VAR}{effects}{DEFA}"\
    
    return left

  def __setitem__(self, key, value):
    match key:
      case "registry_name":
        raise ValueError("Cannot change registry_name outside of difinition")
      case "display_name":
        raise ValueError("Cannot change display_name outside of lang file")
      case "inventories":
        if not isinstance(value, list):
          raise TypeError(f"value must be a list of Inventory not {type(value)}")
        for inventory in value:
          if not isinstance(inventory, Inventory):
            raise TypeError(f"value must be a list of Inventory not {type(inventory)}")
        self.inventories = value
      case "effects":
        if not isinstance(value, list):
          raise TypeError(f"value must be a list of Effect not {type(value)}")
        for effect in value:
          if not isinstance(effect, Effect):
            raise TypeError(f"value must be a list of Effect not {type(effect)}")
        self.effects = value

  def __getitem__(self, key):
    match key:
      case "registry_name":
        return self.__registry_name
      case "display_name":
        return Parser.race_lang(f"{self.__registry_name}")
        
      case "inventories":
        return self.inventories
      case "effects":
        return self.effects
    
    return None


  def register(self):
    Race.registry.register(self)




class Character:
  characters = list["Character"]()
  def __init__(self, char_file: Path, registry_name: str):
    if registry_name in Character.characters:
      raise ValueError(f"Character with registry_name {registry_name} already exists")
    
    if not isinstance(char_file, Path):
      raise ValueError("Path must be an instance of Path")
    if char_file.file_extension != ".char":
      raise ValueError("file must be a char file")

    given_name = ""
    sir_name = ""
    middle_names = []

    race = ""
    age = 0
    gender = ""
    description = ""

    level = 0
    strength = 0
    consitution = 0
    agility = 0
    will = 0
    perception = 0
    inteligence = 0
    charisma = 0
    stat_points = 0

    # open and parse file
    with open(char_file.path, "r") as file:
      char_data = "".join(file.readlines())
      li = dict[str, str]()
      for data in char_data.split(";"):
        data = "".join(data.split("\n"))
        data = "".join(data.split(" "))
        if data == "":
          continue
        li.update({data.split(":")[0]: data.split(":")[1]})

      for i in li:
        match i:
          case "name":
            middle_names = li[i].split(",")
            given_name = middle_names.pop(0)
            sir_name = middle_names.pop(0)
          case "race":
            race = li[i]
          case "age":
            age = int(li[i])
          case "gender":
            gender = li[i]
          case "description":
            description = " ".join(li[i].split("_"))
          case "exp":
            level = int(li[i])
          case "str":
            strength = int(li[i])
          case "con":
            consitution = int(li[i])
          case "agi":
            agility = int(li[i])
          case "wil":
            will = int(li[i])
          case "per":
            perception = int(li[i])
          case "int":
            inteligence = int(li[i])
          case "cha":
            charisma = int(li[i])
          case "points":
            stat_points = int(li[i])
    


    self.__registry_name = None
    self.status = self.Status()
    self.inventory = self.Inventory(race)
    self.info = self.Info(given_name, sir_name, middle_names, race, age, gender, description)

  def __str__(self):
    return f"{self.__registry_name}"



  class Status:
    def __init__(self):
      # self.effects = self.Effects()

      self.__xp = 0
      self.__stat_points = 0

      self.__health_points = 0
      self.__mana_points = 0
      self.__stamina_points = 0
      self.__strength_points = 0
      self.__constitution_points = 0
      self.__agility_points = 0
      self.__will_points = 0
      self.__perseption_points = 0
      self.__intelligence_points = 0
      self.__charisma_points = 0
      self.__health = self.max_health
      self.__mana = self.max_mana
      self.__stamina = self.max_stamina

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
    def xp_to_next_level(self) -> int:
      return self.level * 50 + 100

    @property
    def max_health(self) -> int:
      base = 90
      points = 0
      points += self.__health_points * 5
      points += (self.level * 5)

      points += int((self.constitution * 2 + self.agility * 1.5 + self.strength) // 4 - 1)

      # return base + points + self.effects.max_health

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

      # self.__health += self.effects.health

      return self.__health
     
    @property
    def mana(self) -> int:
      if self.__stamina > self.max_stamina:
        self.__stamina = self.max_stamina

      # self.__mana += self.effects.mana

      return self.__stamina

    @property
    def stamina(self) -> int:
      if self.__mana > self.max_mana:
        self.__mana = self.max_mana
      
      # self.__stamina += self.effects.stamina

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
      points += self.__will_points + self.level
      
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
      points -= (self.__health_points + self.__mana_points + self.__stamina_points + self.__strength_points + self.__constitution_points + self.__agility_points + self.__will_points + self.__intelligence_points + self.__charisma_points)
      points += (self.__stat_points + self.level)

      return points
    
    def __str__(self) -> str:
      f"{CON}{COL}{VAR}{self.level}"
      f"{CON}{COL}{VAR}{self.xp}"
      f"{CON}{COL}{VAR}{self.xp_to_next_level}"
      f"{CON}{COL}{VAR}{self.max_health}"
      f"{CON}{COL}{VAR}{self.max_mana}"
      f"{CON}{COL}{VAR}{self.max_stamina}"
      f"{CON}{COL}{VAR}{self.health}"
      f"{CON}{COL}{VAR}{self.mana}"
      f"{CON}{COL}{VAR}{self.stamina}"
      f"{CON}{COL}{VAR}{self.strength}"
      f"{CON}{COL}{VAR}{self.constitution}"
      f"{CON}{COL}{VAR}{self.agility}"
      f"{CON}{COL}{VAR}{self.intelligence}"
      f"{CON}{COL}{VAR}{self.charisma}"
      f"{CON}{COL}{VAR}{self.stat_points}"
      return f""




  class Inventory:
    def __init__(self, race: str):
      "human",
      "elf",
      "dwarf",
      "orc",
      "kitsune",
      "kobold",
      "tiny",
      "giant",
      "pixie",
      "fairy",
      "sprite",
      "imp",
      "gnome",
      "goblin",
      "hobgoblin",
      "leprechaun",
      "troll"


      # self.__inventories = inventories

    
    def __getitem__(self, key) -> Inventory:
      if isinstance(key, str):
        for inventory in self.__inventories:
          if inventory["name"] == key:
            return inventory
        raise KeyError(f"Invalid key: {key}")
      else:
        raise TypeError(f"key must be int or str not {type(key)}")




  class Info:
    def __init__(self, given_name: str, sir_name: str, middle_names: list[str], race, age: int = -1, gender: str = "random", description: str = "N/A"):
      if not isinstance(given_name, str):
        raise ValueError(f"name must be a str not {type(given_name)}")
      if not isinstance(race, str):
        raise ValueError(f"race must be a str not {type(race)}")
      if age < -1:
        raise ValueError("age must be greater than or equal to -1(set to -1 to disable age)")
      if not isinstance(gender, str):
        raise ValueError(f"gender must be a str not {type(gender)}")
      if not isinstance(description, str):
        raise ValueError(f"description must be a str not {type(description)}")
      self.name = self.Name(given_name, sir_name, middle_names)
      self.race = None
      self.age = age
      self.gender = gender
      self.description = description

    def __str__(self):
      return f"{CON}Name{COL}{VAR}{self.name.full}{DEFA}"\
        f"{f"\n{CON}Race{COL}{VAR}{self.race}" if self.race != None else ""}{DEFA}"\
        f"{f"\n{CON}Age{COL}{VAR}{self.age}" if self.age != -1 else ""}{DEFA}"\
        f"\n{CON}Gender{COL}{VAR}{self.gender}{DEFA}"\
        f"\n{CON}Description{COL}{VAR}{self.description}{DEFA}"\


    class Name:
      def __init__(self, given: str, sir: str, middle: list[str]):
        self.given = given
        self.middle = list(middle)
        self.sir = sir
      
      @property
      def full(self):
        string = ""
        for i in self.middle:
          string += f"{i} "
        return f"{self.given} {string}{self.sir}"