from CommonLib.classes import UUID

__name_registry = list[str]()


class Item:
  def __init__(self, name: str, display_name:str, weight: int,  value: int = 0, stack_size:int=1, description: str = "N/A"):
    if not isinstance(name, str):
      raise ValueError(f"name must be a string not {type(name)}")
    if name in __name_registry:
      raise ValueError(f"Name '{name}' already exists")
    if name.isidentifier():
      raise ValueError(f"Name '{name}' cannot an already register identifier")
    if name[0] == "_":
      raise ValueError(f"Name '{name}' cannot start with underscore")
    if type(name[0]) == int:
      raise ValueError(f"Name '{name}' cannot start with a number")
    if name[-1] == "_":
      raise ValueError(f"Name '{name}' cannot end with underscore")
    for part in name.split("_"):
      if not part.isalnum():
        raise ValueError(f"Name '{name}' cannot contain special characters besides underscore")
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
    


    self.__name = name
    __name_registry.append(name)
    self.__diplay_name = display_name
    self.__weight = weight
    self.__value = value
    self.__stack_size = stack_size
    self.__description = description


  def __str__(self) -> str:
    return f"Item:"\
  f"\nName: {self.__name}"\
  f"{f"\nValue: {self.__value}" if self.__value != -1 else ""}"\
  f"{f"\nStack Size: {self.__stack_size}" if self.__stack_size != 0 else ""}"\
  f"{f"\nWeight: {self.__weight}" if self.__weight != -1 else ""}"\
  f"\nDescription: {self.__description}"\
  
  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "name" | 0:
        return self.__name
      case "weight" | 1:
        if self.__weight == -1:
          raise ValueError("\"weight\" is currently diabled on the item")
        return self.__weight
      case "value" | 2:
        if self.__value == -1:
          raise ValueError("\"value\" is currently diabled on the item")
        return self.__value
      case "stack_size" | 3:
        if self.__stack_size == 0:
          raise ValueError("\"stack_size\" is currently diabled on the item")
        return self.__stack_size
      case "description" | 4:
        return self.__description
      case _:
        raise KeyError(f"Invalid key: {key}")

  def __setitem__(self, key, value):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "name" | 0:
        if not isinstance(value, str):
          raise ValueError(f"name must be a string not {type(value)}")
        self.__name = value
      case "weight" | 1:
        if self.__weight == -1:
          raise ValueError("\"weight\" is currently diabled on the item")
        if not isinstance(value, int):
          raise ValueError(f"weight must be an int not {type(value)}")
        self.__weight = value
      case "value" | 2:
        if self.__value == -1:
          raise ValueError("\"value\" is currently diabled on the item")
        if not isinstance(value, int):
          raise ValueError(f"value must be an int not {type(value)}")
        self.__value = value
      case "stack_size" | 3:
        if self.__stack_size == 0:
          raise ValueError("\"stack_size\" is currently diabled on the item")
        if not isinstance(value, int):
          raise ValueError(f"stack_size must be an int not {type(value)}")
        self.__stack_size = value
      case "description" | 4:
        if not isinstance(value, str):
          raise ValueError(f"description must be a string not {type(value)}")
        self.__description = value
      case _:
        raise KeyError(f"Invalid key: {key}")

  def __eq__(self, value: "Item"):
    return all([
      self["uuid"] == value["uuid"],
      self["name"] == value["name"],
      self["weight"] == value["weight"],
      self["value"] == value["value"],
      self["description"] == value["description"]
    ])



  def set_name(self, new_name: int):
    if not isinstance(new_name, int):
      raise ValueError(f"new_price must be an int not {type(new_name)}")
    self.__value = new_name


  def set_value(self, new_value: int):
    if not isinstance(new_value, int):
      raise ValueError(f"new_price must be an int not {type(new_value)}")
    self.__value = new_value


  def set_value(self, new_value: int):
    if not isinstance(new_value, int):
      raise ValueError(f"new_price must be an int not {type(new_value)}")
    self.__value = new_value




class ItemInstance:
  def __init__(self, item: Item, uuid: UUID):
    if not isinstance(item, Item):
      raise ValueError(f"item must be an Item not {type(item)}")
    self.__uuid = uuid
    self.__item = item
    self.__modifiers = ItemModifiers(self)


  def __str__(self):
    return f"Item:"\
    f"\nName: {self.__item['name']}"\
    f"{f"\nValue: {self.__item['value']}" if self.__item['value']!= -1 else ""}"\
    f"{f"\nStack Size: {self.__item['stack_size']}" if self.__item['stack_size']!= 0 else ""}"\
    f"{f"\nWeight: {self.__item['weight']}" if self.__item['weight']!= -1 else ""}"\
    f"\nDescription: {self.__item['description']}"\
    f"\nModifiers: {self.__modifiers}"\
    f"\nUUID: {self.__uuid}"\

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
  def __init__(self, item: "ItemInstance"):
    if not isinstance(item, ItemInstance):
      raise ValueError(f"item must be an ItemInstance not {type(item)}")
    self.__item = item
    self.__name = None
    self.__value = None
    self.__description = None
    self.__weight = None
    self.__stack_size = None

  def __eq__(self, other:"ItemModifiers"):
    if not isinstance(other, ItemModifiers):
      raise ValueError(f"other must be an ItemModifiers not {type(other)}")
    return all([
      self.__item == other.__item,
      self.__name == other.__name,
      self.__value == other.__value,
      self.__description == other.__description,
      self.__weight == other.__weight,
      self.__stack_size == other.__stack_size
    ])




class Slot:
  def __init__(self, slot_num: int):
    if not isinstance(slot_num, int):
      raise ValueError(f"slot_num must be an int not {type(slot_num)}")
    self.__slot_num = slot_num
    self.__item = None
    self.__amount = 0

  def __str__(self):
    if self.__item is None:
      return f"slot_{self.__slot_num}: \u007Bitem: {self.__item}, amount: {self.__amount}\u007D"
    else:
      return f"slot_{self.__slot_num}: \u007Bitem: {self.__item["item"]["name"]}, amount: {self.__amount}\u007D"

  def __getitem__(self, key):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "slot_num" | 0:
        return self.__slot_num
      case "item" | 1:
        return self.__item
      case "amount" | 2:
        return self.__amount
      case _:
        raise KeyError(f"Invalid key: {key}")
  
  def __setitem__(self, key: str | int, value: ItemInstance | int):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid index type: {type(key)}")
    if not isinstance(value, (ItemInstance, int)):
      raise TypeError(f"value must be an ItemInstance or int not {type(value)}")
    match key:
      case "slot_num" | 0:
        raise AssertionError("Cannot change slot_num after the slot is made. Try creating a new slot and deleting the old one.")
      case "item" | 1:
        if not isinstance(value, (ItemInstance, None)):
          raise TypeError(f"value must be an ItemInstance or None for inedex \"1\" or \"item\" not {type(value)}")
        if value == None:
          self.__amount = 0
        self.__item = value
      case "amount" | 2:
        if not isinstance(value, int):
          raise TypeError(f"value for index \"2\" or \"amount\" must be an int not {type(value)}")
        if self.__item == None:
          self.__amount = 0
          raise ValueError("Cannot change amount while there's no item in this slot")
        if value <= 0:
          raise ValueError(f"amount must be greater than 0 while there's an item in this slot")
        self.__amount = value
      case _:
        raise KeyError(f"Invalid key: {key}")
  
  def __delitem__(self, key: str | int):
    if not isinstance(key, (str, int)):
      raise TypeError(f"Invalid type: {type(key)}")
    match key:
      case "slot_num" | 0:
        raise AssertionError("Cannot change slot_num after the slot is made. Try creating a new slot and deleting the old one.")
      case "item" | 1:
        self.__item = None
        self.__amount = 0
      case "amount" | 2:
        if self.__item != None:
          self.__amount = 1
        else:
          raise AssertionError("Nothing to delete")
      case _:
        raise KeyError(f"Invalid key: {key}")




class Inventory:
  def __init__(self, size: int, weight_limit: int):
    if not isinstance(size, int):
      raise ValueError(f"size must be an int not {type(size)}")
    if size < 0:
      raise ValueError("size must be greater than or qualt to 0(set to 0 to disable size limit)")
    if not isinstance(weight_limit, int):
      raise ValueError(f"weight_limit must be an int not {type(weight_limit)}")
    if weight_limit < 0:
      raise ValueError("weight_limit must be greater than or equal to 0(set to 0 to remove limit)")
    self.__size = size
    self.__weight_limit = weight_limit
    self.__slots = list[Slot]()

    for i in range(size):
      self.__slots.append(Slot(i))
  
  @property
  def items(self):
    return self.__slots


  def __str__(self):
    string = ""
    for slot in self.__slots:
      string += f" {str(slot)}\n"
    return f"Inventory:\n{string}"

  def __getitem__(self, key) -> Slot:
    if isinstance(key, int):
      for slot in self.__slots:
        if slot[0] == key:
          return slot
      raise KeyError(f"Slot {key} does not exist")
    else:
      raise TypeError(f"key must be int not {type(key)}")

  def __setitem__(self, key: str | int, value: ItemInstance | int):
    for slot in self.__slots:
      if slot[0] == key:
        slot[1] = value
        slot[2] = 1

  def __delitem__(self, key):
    if isinstance(key, int):
      end = False
      for index in range(len(self.__slots)):
        if self.__slots[index][0] == key:
          self.__slots.pop(index)
          end = True
          break
      if not end:
        raise KeyError(f"Slot {key} does not exist")
    else:
      raise TypeError(f"key must be int not {type(key)}")



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












ITEM = Item("item 1", 15)
ITEM = Item("item 3", 15)
ITEM = Item("item 2", 15)
INV = Inventory(3, 50)
INS = ItemInstance(ITEM, UUID())

INV.add_slot(5)
INV.add_slot(-1)

# print(INV)

INV[5] = INS

del INV[-1]

print(INV[5][1])