from LocalLibrary import *
from CommonLib.classes import UUID, NotUniqueUUIDError
from CommonLib.functional_classes import staticproperty, staticstr






class Actions(metaclass=staticstr):
  @staticproperty
  def registered() -> list["str"]:
    return check_attr(Actions.__dict__)
  
  @staticproperty
  def all() -> list["Action"]:
    li = []
    for registered in Actions.registered:
      li.append(getattr(Actions, registered))
    return li
  
  @staticproperty
  def names() -> str:
    li = list[str]
    for registered in Actions.registered:
      li.append(getattr(Actions, registered).name)
    return li

  def __str__():
    return "add Actions string"










class Action:
  def __init__(self):
    self.__registry_name = UUID().alphabetic_version
    self.name = "N/A"
    self.description = "N/A"
    self.health_cost = 0
    self.stamina_cost = 0
    self.mana_cost = 0

    self.target = None
    self.action_type = None

  
  @property
  def registry_name(self) -> str:
    return self.__registry_name
  
  def set_health_cost(self, health_cost:int):
    if not isinstance(health_cost, int):
      raise TypeError(f"Health cost must be integer, not {type(health_cost)}")
    if health_cost < 0:
      raise ValueError("Health cost must be a non-negative integer.")
    self.health_cost = health_cost
    return self
  
