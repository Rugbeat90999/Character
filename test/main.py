from CommonLib.classes import UUID

class Item:
  def __init__(self, uuid: UUID, name: str, weight: int,  value: int = 0, stack_size:int=1, description: str = "N/A"):
    if not isinstance(uuid, UUID):
      raise ValueError(f"uuid must be a UUID not {type(uuid)}")
    if not isinstance(name, str):
      raise ValueError(f"name must be a string not {type(name)}")
    if not isinstance(weight, int):
      raise ValueError(f"weight must be an int not {type(weight)}")
    if not isinstance(value, int):
      raise ValueError(f"value must be an int not {type(value)}")
    if not isinstance(stack_size, int):
      raise ValueError(f"stack_size must be an int not {type(stack_size)}")
    if stack_size <= 0:
      raise ValueError("stack_size must be greater than 0")
    if not isinstance(description, str):
      raise ValueError(f"description must be a string not {type(description)}")
    self.__uuid = uuid
    self.__name = name
    self.__weight = weight
    self.__value = value
    self.__stack_size = stack_size
    self.__description = description


  def __str__(self) -> str:
    return f'''Item:
  UUID: {self.__uuid}
  Name: {self.__name}
  value: {self.__value}
  Description: {self.__description}'''
  
  def __get_item__(self, key):
    match type(key):
      case type(""):
        match key:
          case "uuid":
            return self.__uuid
          case "name":
            return self.__name
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
      case _:
        raise TypeError(f"Invalid type: {type(key)}")
  
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


class ItemInstance(Item):
  def __init__(self, item: Item):
    if not isinstance(item, Item):
      raise ValueError(f"item must be an Item not {type(item)}")
    self.__item = item
  


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
    self.__items = self.__Slots(self.__size)
  
  class __Slots:
    def __init__(self, size: int):
      self.__slots = list[dict[str, int | type(None) | Item]]()
      for i in range(size):
        self.__slots.append({"item":None, "num":1})

    def __getitem__(self, key):
      if isinstance(key, int):
        return self.__slots[key]
      # if isinstance(key, str):
      #   names = []
      #   for slot in self.__slots:
      #     slot["item"]
      #   if key not in self.__slots:
      #     raise KeyError(f"Item with name {key} not found")
      # if isinstance(key, Item):
      #   for slot_index in len(self.__slots):
      #     self.__slots[slot_index]
      #   raise ValueError(f"Item {key} not found in inventory")
      # if isinstance(key, UUID):
    
    def __setitem__(self, key, value):
      


ITEM = Item(UUID(), "item 1", 15)

INV = Inventory(3, 50)