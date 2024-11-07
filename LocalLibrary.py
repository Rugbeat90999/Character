from CommonLib.classes import UUID
from CommonLib.functional_classes import staticproperty




class MoneyError(BaseException):
  def __init__(self, message):
    print(f"MoneyError: {message}")




class RegistryError(BaseException):
  def __init__(self, message):
    print(f"RegistryError: {message}")




class Fraction:
  '''
  only for looks, not usable in math functions
  '''
  def __init__(self, numerator: int, denominator:int):
    self.numerator = numerator
    self.denominator = denominator
  
  def __str__(self):
    return f"{self.numerator}/{self.denominator}"




class UUIDCounter:
  def __init__(self, signature: int):
    

    self.type = 0
    self.minor_type = 0
    self.signature = ""
    self.buff_type = 0
    self.number = 0

    self.set_signature(signature)
  
  def __str__(self):
    return self.__format__()
  
  def __format__(self, format_spec: str = "default"):
    match format_spec:
      case _:
        type = str(self.type)
        while len(type) < 8:
          type = "0" + type
        minor_type = str(self.minor_type)
        while len(minor_type) < 4:
          minor_type = "0" + minor_type
        buff_type = str(self.buff_type)
        while len(buff_type) < 4:
          buff_type = "0" + buff_type
        number = str(self.number)
        while len(number) < 12:
          number = "0" + number
        self.next_number()
        return f"{type}-{minor_type}-{self.signature}-{buff_type}-{number}"
      
  def set_signature(self, signature:int):
    if signature < 0:
      raise ValueError("Signature must be a positive integer.")
    if len(str(signature)) > 4:
      raise ValueError("Signature can only have at most 4 digits.")
    while len(str(signature)) < 4:
      signature = "0" + str(signature)
    self.signature = signature
  
  def next_type(self):
    self.type += 1
    self.minor_type = 0
    self.buff_type = 0
    self.number = 0
    if self.type > 99999999:
      self.type = 0
      self.set_signature(int(self.signature)+1)
    return self
  
  def next_minor_type(self):
    self.minor_type += 1
    self.buff_type = 0
    self.number = 0
    if self.minor_type > 9999:
      self.minor_type = 0
      self.set_signature(int(self.signature)+1)
    return self
    
  def next_buff_type(self):
    self.buff_type += 1
    self.number = 0
    if self.buff_type > 9999:
      self.buff_type = 0
      self.set_signature(int(self.signature)+1)
    return self
    
  def next_number(self):
    self.number += 1
    if self.number > 999999999999:
      self.number = 0
      self.set_signature(int(self.signature)+1)
    return self




def UUID_search(uuid:UUID, search_list:list):
  for index in range(len(search_list)):
    if uuid == search_list[index].uuid:
      return index
  return -1


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