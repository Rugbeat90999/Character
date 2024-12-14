from CommonLib.classes import UUID, Path, OutputColors
from CommonLib.constants import Output
from CommonLib.functional_classes import staticproperty
from CommonLib.functions import debug
import json



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
    race_lang = lang()["prints"]
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
    neg = False

    for char in str(number):
      if char == "-":
        neg = True
        continue
      value += numeral_lang[char]


    if numeral_direction == "left":
      value_change_list = []
      for char in value:
        value_change_list.insert(0, char)
      value = "".join(value_change_list)

    return f"{Parser.print_lang("-")}{value}" if neg else value


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
      tag_str += f"{Output.VAR}{tag}{Output.DEFA}{Output.COM}"
    tag_str = tag_str.rstrip(Output.COM)

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


  @staticmethod
  def character_data(data_dict: dict):
    temp = []
    for i in data_dict:
      temp.append(data_dict[i])
    return tuple(temp)


  @staticmethod
  def info_lang(info: str):
    race_lang = lang()["info"]
    try:
      info = race_lang[f"{info}"]
      info.strip()
      if info == "":
        info = info
    except:
      info = info
    return info






class Registry:
  def __init__(self, registry_name: str):
    self.__registry = list()
    self.__registry_name = registry_name

  def __repr__(self):
    return f"{Output.CLS}Registry{Output.ERR}({self.__registry_name}{Output.COM} {len(self.registry)}){Output.DEFA}"

  @property
  def registry(self):
    return self.__registry
  
  @property
  def names(self):
    return [registry_item.registry_name for registry_item in self.__registry]


  def get(self, name: str):
    for item in self.__registry:
      if item.registry_name == name:
        return item
    raise ValueError(f"registry item {name.__repr__()} does not exist")


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
    
    self.__registry.append(item)





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

  def __repr__(self):
    return f"{Output.CLS}{self.tag}{Output.DEFA}"

  @property
  def tag(self):
    tag_list = []
    parent = self.__parent
    while True:
      tag_list.insert(0, parent.current_tag)
      parent = parent.parent
      if parent == "Base":
        break

    temp = ""
    f"{".".join(tag_list)}.{self.__tag}" 
    for tag in tag_list:
      temp += f"{OutputColors(color="cyan")}{tag}{OutputColors(color="green")}."
    temp += f"{OutputColors(color="cyan")}{self.current_tag}{Output.DEFA}"
    return temp

  @property
  def current_tag(self):
    return self.__tag

  @property
  def parent(self):
    return self.__parent




# Item
class Item:
  registry = Registry("ITEM")
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
    word_direction = lang()["word_direction"]

    value = Parser.number_lang(self.__value)
    stack_size = Parser.number_lang(self.__stack_size)
    weight = Parser.number_lang(self.__weight)

    display_name, description = Parser.item_lang(self.__registry_name)

    tags = Parser.Tags(self.__tags)



    right = f"{Output.TITLE}{Parser.print_lang("item")}{Output.COL} {Output.DEFA}"\
      f"\n{Output.CON} {Parser.print_lang("registry_name")}{Output.COL} {Output.VAR}{self.registry_name}{Output.DEFA}"\
      f"\n{Output.CON} {Parser.print_lang("display_name")}{Output.COL} {Output.VAR}{display_name}{Output.DEFA}"\
      f"{f"\n{Output.CON} {Parser.print_lang("value")}{Output.COL} {Output.VAR}{value}" if self.__value != -1 else ""}{Output.DEFA}"\
      f"{f"\n{Output.CON} {Parser.print_lang("stack_size")}{Output.COL} {Output.VAR}{stack_size}" if self.__stack_size != 0 else ""}{Output.DEFA}"\
      f"{f"\n{Output.CON} {Parser.print_lang("weight")}{Output.COL} {Output.VAR}{weight}" if self.__weight != -1 else ""}{Output.DEFA}"\
      f"\n{Output.CON} {Parser.print_lang("description")}{Output.COL} {Output.VAR}{description}{Output.DEFA}"\
      f"\n{Output.CON} {Parser.print_lang("tags")}{Output.COL} {Output.VAR}{tags}{Output.DEFA}"\

    left = f"{Output.COL}{Output.TITLE}{Parser.print_lang("item")}{Output.DEFA}"\
      f"\n{Output.VAR}{self.registry_name}{Output.COL}{Output.CON}{Parser.print_lang("registry_name")}{Output.DEFA}"\
      f"\n{Output.VAR}{display_name}{Output.COL}{Output.CON}{Parser.print_lang("display_name")}{Output.DEFA}"\
      f"{f"\n{Output.VAR}{value}{Output.COL}{Output.CON}{Parser.print_lang("value")}" if self.__value != -1 else ""}{Output.DEFA}"\
      f"{f"\n{Output.VAR}{stack_size}{Output.COL}{Output.CON}{Parser.print_lang("stack_size")}" if self.__stack_size != 0 else ""}{Output.DEFA}"\
      f"{f"\n{Output.VAR}{weight}{Output.COL}{Output.CON}{Parser.print_lang("weight")}" if self.__weight != -1 else ""}{Output.DEFA}"\
      f"\n{Output.VAR}{description}{Output.COL}{Output.CON}{Parser.print_lang("description")}{Output.DEFA}"\
      f"\n{Output.VAR}{tags}{Output.COL}{Output.CON}{Parser.print_lang("tags")}{Output.DEFA}"\

    return left if word_direction == "left" else right
  
  def __repr__(self):
    return f"{Output.CLS}Item{Output.ERR}({self.__registry_name}){Output.DEFA}"

  
  @property
  def registry_name(self):
    return self.__registry_name
  
  @property
  def display_name(self):
    return Parser.item_lang(self.__registry_name)[0]
  
  @property
  def weight(self):
    return self.__weight
  
  @property
  def value(self):
    return self.__value
  
  @property
  def stack_size(self):
    return self.__stack_size
  
  @property
  def description(self):
    return Parser.item_lang(self.__description)[1]


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


  def set_value(self, new_value: int):
    if self.__value == -1:
      raise AssertionError("weight cannot be set as it's diabled in this item's registry")

    if not isinstance(new_value, int):
      try:
        new_value = Parser.lang_number(new_value)
      except:
        raise ValueError(f"weight must be an int not {type(new_value)}")

    self.__value = new_value
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
    return f"{Output.TITLE}Item Instance{Output.COL}{Output.DEFA}"\
    f"\n {Output.CON}UUID{Output.COL} {Output.VAR}{self.__uuid}{Output.DEFA}"\
    f"\n {Output.CON}Name{Output.COL} {Output.VAR}{self.__item['name']}{Output.DEFA}"\
    f"\n {Output.CON}Display Name{Output.COL} {Output.VAR}{self.__item['display_name']}{Output.DEFA}"\
    f"{f"\n {Output.CON}Value{Output.COL} {Output.VAR}{self.__item['value']}" if self.__item['value'] != -1 else ""}{Output.DEFA}"\
    f"{f"\n {Output.CON}Stack Size{Output.COL} {Output.VAR}{self.__item['stack_size']}" if self.__item['stack_size'] != 0 else ""}{Output.DEFA}"\
    f"{f"\n {Output.CON}Weight{Output.COL} {Output.VAR}{self.__item['weight']}" if self.__item['weight'] != -1 else ""}{Output.DEFA}"\
    f"\n {Output.CON}Description{Output.COL} {Output.VAR}{self.__item['description']}{Output.DEFA}"\
    f"\n {Output.CON}Modifiers{Output.COL} {Output.VAR}{self.__modifiers}{Output.DEFA}"\

  def __repr__(self):
    return f"{Output.CLS}ItemInstance{Output.ERR}({self.__item["registry_name"]}, {self.__uuid}){Output.DEFA}"

  @property
  def uuid(self):
    return self.__uuid
  @property
  def registry_name(self):
    return self.__item.registry_name
  @property
  def display_name(self):
    return self.__item.display_name
  @property
  def value(self):
    return self.__item.value
  @property
  def stack_size(self):
    return self.__item.stack_size
  @property
  def weight(self):
    return self.__item.weight
  @property
  def description(self):
    return self.__item.description
  @property
  def modifiers(self):
    return self.__modifiers




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
    return f"{Output.CBO}\u007b{f"{Output.CON}display{Output.COL} {Output.VAR}{self.__display_name}{Output.COM} " if self.__display_name != None else ""}{f"{Output.CON}value{Output.COL} {Output.VAR}{self.__value}{Output.COM} " if self.__value != None else ""}\
{f"{Output.CON}weight{Output.COL} {Output.VAR}{self.__weight}{Output.COM} " if self.__weight != None else ""}\
{f"{Output.CON}stack_size{Output.COL} {Output.VAR}{self.__stack_size}{Output.COM} " if self.__stack_size != None else ""}\
{f"{Output.CON}description{Output.COL} {Output.VAR}{self.__description}" if self.__description != None else ""}\
{Output.CBC}\u007d{Output.DEFA}"\

  
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
          raise ValueError(f"tags must only contain {Output.CLS}Tag{Output.ERR} not {type(tag)}")
    self.__slot_num = slot_num
    self.__slot_name = slot_name
    self.__item = None
    self.__amount = 0
    self.__tag_list = tags

  def __str__(self):
    tags = None
    if self.__tag_list != None:
      tags = f"{Output.SBO}"
      for tag in self.__tag_list:
        tags += f"{tag.tag}{Output.COM}"

      tags = tags.rstrip(Output.COM)

      tags += f"{Output.SBC}"
    

    left = f"{Output.TITLE}{Parser.print_lang("slot_")}{Parser.number_lang(self.__slot_num)}{Output.COL}"\
      f"{Output.CBO}"\
      f"{f"{Output.CON}slot_name{Output.COL} {Output.VAR}\"{self.__slot_name}\"{Output.COM}" if self.__slot_name != "N/A" else ""}"\
      f"{f"{Output.CON}item{Output.COL} {Output.VAR}{self.__item.display_name}" if self.__item != None else f"{Output.CON}item{Output.COL} {Output.VAR}{self.__item}"}"\
      f"{Output.COM}{Output.CON}amount{Output.COL} {Output.VAR}{self.__amount}{Output.DEFA}"\
      f"{f"{Output.COM}{Output.CON}tag_list{Output.COL} {tags}{Output.DEFA}" if self.__tag_list != None else f"{Output.COM}{Output.CON}tag_list{Output.COL} {Output.SBO}{Output.SBC}{Output.DEFA}"}"\
      f"{Output.CBC}"\

    return left

  def __repr__(self):
    return f"{Output.CLS}Slot{Output.ERR}({self.__slot_num}{Output.COM}{Output.ERR}{self.__slot_name}){Output.DEFA}"

  @property
  def slot_num(self):
    return self.__slot_num

  @property
  def slot_name(self):
    return self.__slot_name

  @property
  def display_name(self):
    return Parser.slot_lang(self.__slot_name)

  @property
  def item(self):
    return self.__item

  @property
  def amount(self):
    return self.__amount

  @property
  def tags(self):
    return self.__tag_list

  @property
  def weight(self):
    if self.__item == None:
      return 0
    return self.__item.weight * self.__amount


  def set_name(self, name):
    if not isinstance(name, str):
      raise ValueError(f"name must be a string not {type(name)}")
    self.__slot_name = name
    return self


  def add_tag(self, *tag_or_tags: Tag):
    for tag in tag_or_tags:
      if not isinstance(tag, (Tag, None)):
        raise ValueError(f"tag_or_tags must be a either Tag or list of Tag not {type(tag_or_tags)}")
      if tag == None:
        self.__tag_list = None
        break

      if self.__tag_list == None:
        self.__tag_list = [tag]
      else:
        self.__tag_list.append(tag)


  def remove_tag(self, *tag_or_tags: Tag):
    for tag in tag_or_tags:
      if not isinstance(tag, Tag):
        raise ValueError(f"tag_or_tags must be a either Tag or list of Tag not {type(tag_or_tags)}")
      else:
        self.__tag_list.remove(tag)


  def set_item(self, item: ItemInstance):
    if not isinstance(item, ItemInstance):
      raise ValueError(f"item must be an Item not {type(item)}")
    self.__item = item
    self.__amount = 1
    return self


  def set_amount(self, amount: int):
    if not isinstance(amount, int):
      raise ValueError(f"amount must be an int not {type(amount)}")
    if amount < 0:
      raise ValueError("amount must be greater than or equal to 0")
    self.__amount = amount
    return self
  
  
  def clear(self):
    self.__item = None
    self.__amount = 0
    return self






class Inventory:
  registry = Registry("INVENTORY")
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
      tag_str = ""
      if slot.tags != None:
        for tag in slot.tags:
          tag_str += f"{tag.tag}"

      string += f"\n {Output.TITLE}{Parser.print_lang("slot_")}{Parser.number_lang(f"{slot.slot_num}")}{Output.COL} "\
      f"{Output.CBO}"\
      f"{f"{Output.CON}{Parser.print_lang("name")}{Output.COL} {Output.VAR}{slot.slot_name}{Output.COM}" if slot.slot_name != "N/A" else ""}"\
      f"{Output.CON}{Parser.print_lang("item")}{Output.COL} {f"{Output.VAR}{Parser.item_lang(slot.item.registry_name)}" if slot.item != None else f"{Output.VAR}{None}"}"\
      f"{Output.COM}{Output.CON}{Parser.print_lang("amount")}{Output.COL} {Output.VAR}{Parser.number_lang(slot.amount)}"\
      f"{f"{Output.COM}{Output.CON}{Parser.print_lang("tag_list")}{Output.COL} {Output.VAR}{tag_str}" if tag_str != "" else ""}"\
      f"{Output.CBC}"\

    left = f"{Output.TITLE}{self.display_name}{Output.COL}"\
    f"{string}"\
    f"{Output.DEFA}"
    # left = f"{string}{Output.DEFA}"
    return left

  def __repr__(self):
    return f"{Output.CLS}Inventory{Output.ERR}({self.__registry_name}){Output.DEFA}"

  @property
  def slots(self):
    return self.__slots

  @property
  def registry_name(self):
    return self.__registry_name

  @property
  def display_name(self):
    return Parser.inventory_lang(self.__registry_name)

  @property
  def weight(self):
    total_weight = 0
    for slot in self.__slots:
      if slot.item != None:
        total_weight += slot.weight
    return total_weight


  def add_slot(self, slot_num:int):
    if not isinstance(slot_num, int):
      raise ValueError(f"slot_num must be an int not {type(slot_num)}")
    for slot in self.__slots:
      if slot.slot_num == slot_num:
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




class InventoryInstance:
  def __init__(self, inventory: Inventory):
    self.__slots = list[Slot]()
    for slot_num in range(len(inventory.slots)):
      self.__slots.append(Slot(slot_num, inventory.slots[slot_num].slot_name, inventory.slots[slot_num].tags))
    
    self.__registry_name = inventory.registry_name
  
  def __str__(self):
    string = ""
    for slot in self.__slots:
      string += f"\n {str(slot)}"

    return f"{Output.TITLE}{self.display_name}{Output.COL}{Output.DEFA}{string}{Output.DEFA}"

  def __repr__(self):
    return f"{Output.CLS}InventoryInstance{Output.ERR}({self.__registry_name}){Output.DEFA}"

  @property
  def slots(self):
    return self.__slots

  @property
  def registry_name(self):
    return self.__registry_name

  @property
  def display_name(self):
    return Parser.inventory_lang(self.__registry_name)

  @property
  def weight(self):
    total_weight = 0
    for slot in self.__slots:
      if slot.item != None:
        total_weight += slot.weight
    return total_weight




class Effect:
  registry = Registry("EFFECT")
  def __init__(self, registry_name: str):
    self.__registry_name = registry_name
    self.__funcitons = []

  def __repr__(self):
    return f"{Output.CLS}Effect{Output.ERR}({self.__registry_name}){Output.DEFA}"

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
  registry = Registry("RACE")
  def __init__(self, registry_name: str, inventories: list[Inventory], race_effects: list[Effect]):
    if not isinstance(inventories, list):
      raise ValueError(f"inventories must be a list of Inventories not {type(inventories)}")

    temp = list[Inventory]()
    temp = inventories.copy()

    for _ in range(len(temp)):
      inv1 = temp.pop()
      for inv2 in temp:
        if inv1.registry_name == inv2.registry_name:
          raise ValueError(f"Inventory with registry_name {inv1.registry_name} already added to this race")


    
    self.__registry_name = registry_name
    self.__inventories = inventories
    self.__effects = race_effects



  def __str__(self):
    inventories = ""
    for inventory in self.__inventories:
      inventories += f"{Output.VAR}{inventory.display_name}{Output.COM}"
    inventories = inventories.rstrip(f"{Output.COM}")

    effects = None
    # effects = ""
    # for effect in self.__effects:
    #   effects += f"{Output.VAR}{effect.display_name}{Output.COM}"
    # effects = effects.rstrip(f"{Output.COM}")

    
    left = f"{Output.TITLE}{Parser.print_lang("race")}{Output.COL}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("registry_name")}{Output.COL} {Output.VAR}{self.__registry_name}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("display_name")}{Output.COL} {Output.VAR}{self.display_name}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("inventories")}{Output.COL} {inventories}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("effects")}{Output.COL} {Output.VAR}{effects}{Output.DEFA}"\
    
    return left
  
  def __repr__(self):
    return f"{Output.CLS}Race{Output.ERR}({self.__registry_name}){Output.DEFA}"

  @property
  def registry_name(self):
    return self.__registry_name

  @property
  def display_name(self):
    return Parser.race_lang(f"{self.__registry_name}")

  @property
  def inventories(self):
    return self.__inventories

  @property
  def effects(self):
    return self.__effects


  def register(self):
    Race.registry.register(self)
    return self




class Experience:
  def __init__(self, xp, stats_points):
    self.__xp = xp
    self.__stats_points = stats_points
  

  @property
  def xp(self):
    level = 0
    xp = self.__xp
    while xp >= (level * 50 + 100):
      xp -= (level * 50 + 100)
      level += 1

    return xp


  @property
  def xp_to_next_level(self):
    return self.level * 50 + 100


  @property
  def level(self):
    level = 0
    xp = self.__xp
    while xp >= (level * 50 + 100):
      xp -= (level * 50 + 100)
      level += 1

    return level

  @property
  def experience_points(self):
    return self.__xp

  @property
  def stats_points(self):
    return self.__stats_points


  # def add_points(self, amount:int):
  #   pass

  # def remove_points(self, amount:int):
  #   pass

  # def set_points(self, amount:int):
  #   pass

  # def add_xp(self, amount:int):
  #   pass

  # def remove_xp(self, amount:int):
  #   pass

  # def set_xp(self, amount:int):
  #   pass




class Character:
  characters = Registry("CHARACTER")
  def __init__(self, char_file: Path, registry_name: str):
    if registry_name in Character.characters.registry:
      raise ValueError(f"Character with registry_name {registry_name} already exists")
    
    if not isinstance(char_file, Path):
      raise ValueError("Path must be an instance of Path")
    if char_file.file_extension != ".char":
      raise ValueError("file must be a char file")
    with open(char_file.path, "r") as char:
      file = json.load(char)

    race = Race.registry.get(file["info"]["race"])
    
    self.__registry_name = registry_name

    level = Parser.character_data(file["stats"]["level"])
    pool = Parser.character_data(file["stats"]["pool"])
    definite = Parser.character_data(file["stats"]["definite"])

    self.status = self.Status(registry_name, level, pool, definite)
    self.inventory = self.Inventory(registry_name, race.inventories)
    self.info = self.Info(registry_name, (file["info"]["name"]["given"], file["info"]["name"]["sir"], file["info"]["name"]["middle"]), race, (file["info"]["age"], file["info"]["gender"], file["info"]["description"]))

  def __str__(self):
    left = f"{Output.TITLE}{Parser.print_lang("character")}{Output.COL} {Output.VAR}{self.__registry_name} {Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("name")}{Output.COL} {Output.VAR}{self.info.name.full}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("race")}{Output.COL} {Output.VAR}{Parser.race_lang(self.info.race.display_name)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("experiance_points")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.xp)}/{Parser.number_lang(self.status.xp_to_next_level)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("level")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.level)}{Output.DEFA}"\
    f"\n"\
    f"\n {Output.CON}{Parser.print_lang("vitality")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.vitality.current)}/{Parser.number_lang(self.status.vitality.max)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("mana")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.stamina.current)}/{Parser.number_lang(self.status.stamina.max)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("stamina")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.mana.current)}/{Parser.number_lang(self.status.stamina.max)}{Output.DEFA}"\
    f"\n"\
    f"\n {Output.CON}{Parser.print_lang("constitution")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.constitution)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("strength")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.strength)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("agility")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.agility)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("will")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.will)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("intelligence")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.intelligence)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("perception")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.perception)}{Output.DEFA}"\
    f"\n {Output.CON}{Parser.print_lang("stat_points")}{Output.COL} {Output.VAR}{Parser.number_lang(self.status.stat_points)}{Output.DEFA}"\

    return left

  def __repr__(self):
    return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.DEFA}"


  def register(self):
    Character.characters.register(self)
    return self




  class Status:
    def __init__(self, registry_name:str, level:tuple[int, int], pool:tuple[tuple[int, int], tuple[int, int], tuple[int, int]], definite:tuple[int, int, int, int, int, int]):
      # self.effects = self.Effects()
      self.__registry_name = registry_name

      self.__experience = Experience(level[0], level[1])


      self.__vitality_points = pool[0]
      self.__stamina_points = pool[1]
      self.__mana_points = pool[2]

      self.__constitution_points = definite[0]
      self.__strength_points = definite[1]
      self.__agility_points = definite[2]
      self.__will_points = definite[3]
      self.__intelligence_points = definite[4]
      self.__perception_points = definite[5]


      self.vitality = self.Vitality(self.__registry_name, self.__vitality_points, self.__experience)
      self.stamina = self.Stamina(self.__registry_name, self.__stamina_points, self.__experience, self.__definite_points)
      self.mana = self.Mana(self.__registry_name, self.__mana_points, self.__experience, self.__definite_points)

    def __str__(self) -> str:
      left = f"{Output.TITLE}{Parser.print_lang("character")}{Output.COL}"\
      f"\n {Output.CON}{Parser.print_lang("experiance_points")}{Output.COL} {Output.VAR}{self.__experience.xp}/{self.__experience.xp_to_next_level}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("level")}{Output.COL} {Output.VAR}{self.__experience.level}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("vitality")}{Output.COL} {Output.VAR}{Parser.number_lang(self.vitality.current)}/{Parser.number_lang(self.vitality.max)}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("mana")}{Output.COL} {Output.VAR}{Parser.number_lang(self.stamina.current)}/{Parser.number_lang(self.stamina.max)}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("stamina")}{Output.COL} {Output.VAR}{Parser.number_lang(self.mana.current)}/{Parser.number_lang(self.stamina.max)}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("constitution")}{Output.COL} {Output.VAR}{self.constitution}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("strength")}{Output.COL} {Output.VAR}{self.strength}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("agility")}{Output.COL} {Output.VAR}{self.agility}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("will")}{Output.COL} {Output.VAR}{self.will}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("intelligence")}{Output.COL} {Output.VAR}{self.intelligence}{Output.DEFA}"\
      f"\n {Output.CON}{Parser.print_lang("perception")}{Output.COL} {Output.VAR}{self.perception}{Output.DEFA}"\

      return left

    def __repr__(self) -> str:
      return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Status{Output.DEFA}"

    @property
    def __pool_points(self):
      return (self.__vitality_points, self.__stamina_points, self.__mana_points)

    @property
    def __level_points(self):
      return (self.__xp_points, self.__stat_points)

    @property
    def __definite_points(self):
      return (self.__constitution_points, self.__strength_points, self.__agility_points, self.__will_points, self.__intelligence_points, self.__perception_points)

    @property
    def level(self):
      return self.__experience.level

    @property
    def xp(self):
      return self.__experience.xp

    @property
    def xp_to_next_level(self):
      return self.__experience.xp_to_next_level

    @property
    def constitution(self) -> int:
      base = 10
      points = 0
      points += self.__constitution_points + self.__experience.level
      
      return base + points

    @property
    def strength(self) -> int:
      base = 10
      points = 0
      points += self.__strength_points + self.__experience.level
      
      return base + points

    @property
    def agility(self) -> int:
      base = 10
      points = 0
      points += self.__agility_points + self.__experience.level
      
      return base + points

    @property
    def will(self) -> int:
      base = 10
      points = 0
      points += self.__will_points + self.__experience.level
      
      return base + points

    @property
    def intelligence(self) -> int:
      base = 10
      points = 0
      points += self.__intelligence_points + self.__experience.level
      
      return base + points

    @property
    def perception(self) -> int:
      base = 10
      points = 0
      points += self.__perception_points + self.__experience.level
      
      return base + points

    @property
    def stat_points(self) -> int:
      points = 5
      # points -= ()
      points += (self.__experience.stats_points + self.__experience.level)

      return points




    class Vitality:
      def __init__(self, registry_name, vit_stats:tuple[int, int], experience:Experience):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        self.__registry_name = registry_name
        self.__experience = experience
        self.__vitality_points = vit_stats[1]
        self.current = vit_stats[0]

      def __str__(self) -> str:
        return f"{Output.CON}{Parser.print_lang('vitality')}{Output.COL} {Output.VAR}{self.current}/{self.max}{Output.DEFA}"

      def __repr__(self):
        return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Status.Vitality{Output.DEFA}"

      @property
      def max(self):
        return self.__experience.level + (self.__vitality_points * 10) + 100


      def update(self, experience: Experience, vitality_points: int):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        if not isinstance(vitality_points, int):
          raise TypeError(f"Can only update with type \"int\" but got {type(vitality_points)}")
        self.__experience = experience
        self.__vitality_points = vitality_points
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def damage(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current -= value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def heal(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current += value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0




    class Stamina:
      def __init__(self, registry_name, stamina_points:tuple[int, int], experience:Experience, stats:tuple[int, int, int, int, int, int]):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        self.__registry_name = registry_name
        self.__experience = experience
        self.__stamina_points = stamina_points[1]
        self.current = stamina_points[0]
        self.__stats = stats

      def __str__(self) -> str:
        return f"{Output.CON}{Parser.print_lang('stamina')}{Output.COL} {Output.VAR}{self.current}/{self.max}{Output.DEFA}"

      def __repr__(self):
        return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Status.Stamina{Output.DEFA}"

      @property
      def max(self):
        return self.__experience.level + self.__stamina_points + 100 + int((self.__stats[0] * 2) + (self.__stats[1] * 1.5) + (self.__stats[3]))


      def update(self, stamina_points: int, experience: Experience, stats: tuple[int, int, int, int, int, int]):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        if not isinstance(stamina_points, int):
          raise TypeError(f"Can only update with type \"int\" but got {type(stamina_points)}")
        self.__experience = experience
        self.__stamina_points = stamina_points
        self.__stats = stats
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def damage(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current -= value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def heal(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current += value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0




    class Mana:
      def __init__(self, registry_name, mana_points:tuple[int, int], experience:Experience, stats:tuple[int, int, int, int, int, int]):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        self.__registry_name = registry_name
        self.__experience = experience
        self.__mana_points = mana_points[1]
        self.current = mana_points[0]
        self.__stats = stats

      def __str__(self) -> str:
        return f"{Output.CON}{Parser.print_lang('mana')}{Output.COL} {Output.VAR}{self.current}/{self.max}{Output.DEFA}"

      def __repr__(self):
        return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Status.Mana{Output.DEFA}"

      @property
      def max(self):
        return self.__experience.level + self.__mana_points + 100 + int((self.__stats[3] * 2) + (self.__stats[4] * 1.5) + (self.__stats[5]))


      def update(self, experience: Experience, mana_points: int, stats:tuple[int, int, int, int, int, int]):
        if not isinstance(experience, Experience):
          raise TypeError(f"Can only update with type \"Experience\" but got {type(experience)}")
        if not isinstance(mana_points, int):
          raise TypeError(f"Can only update with type \"int\" but got {type(mana_points)}")
        self.__experience = experience
        self.__mana_points = mana_points
        self.__stats = stats
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def damage(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current -= value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0


      def heal(self, value:int):
        if not isinstance(value, int):
          raise TypeError(f"Can only damage with type \"int\" but got {type(value)}")
        self.current += value
        if self.current > self.max:
          self.current = self.max
        elif self.current < 0:
          self.current = 0



  # links inventory instances to char so they can be used
  class Inventory:
    def __init__(self, registy_name: str, inventories: list[Inventory]):
      if isinstance(inventories, list):
        for i in inventories:
          if not isinstance(i, Inventory):
            raise TypeError(f"list must contain only \"InventoryInstance\" but got {type(i)}")
      else:
        raise TypeError(f"invetories must be a list but got {type(inventories)}")
      
      self.__inventories = list[InventoryInstance]()
      for i in inventories:
        self.__inventories.append(InventoryInstance(i))

      self.__registry_name = registy_name
    
    def __str__(self):

      inventories = ""
      for inventory in self.__inventories:
        slots = ""
        for slot in inventory.slots:
          slots += f"\n  {Output.CON}{Parser.print_lang("slot_")}{slot.slot_num}{Output.COL} {Output.VAR}{slot.amount} {f"{slot.item.display_name}" if slot.item != None else None}{Output.DEFA}"\

        inventories += f" {Output.CON}{inventory.display_name}{Output.COL}{Output.DEFA}"\
        f"{slots}\n\n"\
        
      inventories = inventories.rstrip("\n\n")


      left = f"{Output.TITLE}{Parser.print_lang("inventory")}{Output.COL} {Output.VAR}{self.__registry_name}{Output.DEFA}"\
      f"\n{inventories}{Output.DEFA}"\

      return left


    def __repr__(self):
      return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Inventory{Output.DEFA}"

    def __getitem__(self, key) -> Inventory:
      if isinstance(key, str):
        for inventory in self.__inventories:
          if inventory.registry_name == key:
            return inventory
        raise KeyError(f"Invalid key: {key}")
      else:
        raise TypeError(f"key must be int or str not {type(key)}")



  # details of char that don't effect common gameplay
  class Info:
    def __init__(self, registry_name: str, name_tuple:tuple[str, str, list[str]], race, data_tuple:tuple[int, str, str]):
      if not isinstance(name_tuple[0], str):
        raise ValueError(f"name must be a str not {type(name_tuple[0])}")
      if not isinstance(race, Race):
        raise ValueError(f"race must be of type \"Race\" not {type(race)}")
      if data_tuple[0] < -1:
        raise ValueError("age must be greater than or equal to -1(set to -1 to disable age)")
      if not isinstance(data_tuple[1], str):
        raise ValueError(f"gender must be a str not {type(data_tuple[1])}")
      if not isinstance(data_tuple[2], str):
        raise ValueError(f"description must be a str not {type(data_tuple[2])}")
      self.__registry_name = registry_name
      self.__name = self.Name(name_tuple[0], name_tuple[1], name_tuple[2])
      self.__race = race
      self.__age = data_tuple[0]
      self.__gender = data_tuple[1]
      self.__description = data_tuple[2]
      self.lore = ""


    def __str__(self):
      left = f"{Output.CON}Name{Output.COL} {Output.VAR}{self.name.full}{Output.DEFA}"\
        f"{f"\n{Output.CON}Race{Output.COL} {Output.VAR}{self.race.display_name}" if self.race != None else ""}{Output.DEFA}"\
        f"{f"\n{Output.CON}Age{Output.COL} {Output.VAR}{self.age}" if self.age != -1 else ""}{Output.DEFA}"\
        f"\n{Output.CON}Gender{Output.COL} {Output.VAR}{Parser.info_lang(self.gender)}{Output.DEFA}"\
        f"\n{Output.CON}Description{Output.COL} {Output.VAR}{self.description}{Output.DEFA}"\

      return left

    def __repr__(self):
      return f"{Output.CLS}Character{Output.ERR}({self.__registry_name}){Output.CLS}.Info{Output.DEFA}"

    @property
    def name(self):
      return self.__name
    
    @property
    def race(self):
      return self.__race
    
    @property
    def age(self):
      return self.__age
    
    @property
    def gender(self):
      return self.__gender
    
    @property
    def description(self):
      return self.__description


    def set_lore(self, lore: str):
      self.lore = lore
      return self



    #name class meant only for info class
    class Name:
      def __init__(self, given: str, sir: str, middle: list[str]):
        self.__given = given
        self.__middle = list[str](middle)
        self.__sir = sir

      @property
      def full(self):
        string = ""
        for i in self.middle:
          string += f"{i} "
        return f"{self.given} {string}{self.sir}"
      
      @property
      def given(self):
        return self.__given
      
      @property
      def middle(self):
        return self.__middle
      
      @property
      def sir(self):
        return self.__sir