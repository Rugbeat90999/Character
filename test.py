from typing import overload

class A:
  def __init__(self):
    self.a = "a"
    self.__ab = "ab"

  @property
  def ab(self) -> str:
    return self.__ab
  
  def method(self):
    print("method A")
  
  def set_ab(self, ab: str):
    if not isinstance(ab, str):
      raise TypeError("AB must be a string.")
    self.__ab = ab

class B(A):
  def __init__(self):
    super().__init__()
    self.b = "b"
    self.bludgeonable = False

  # @property
  # def ab(self) -> str:
  #   return self.__ab

  @overload
  def method(self, string:str) -> str:...

  @overload
  def method(self, number:int) -> str:...

  def method(self, value) -> str:
    if isinstance(value, str):
      print(f"Method B string: {value}")
    elif isinstance(value, int):
      print(f"Method B number: {value}")
    else:
      raise TypeError("You must provide either a string or a number")
  
  def set_bludonable(self, bludgeonable:bool):
    if not isinstance(bludgeonable, bool):
      raise TypeError("Bludgeonability must be a boolean value.")
    self.bludgeonable = bludgeonable
    return self
  
  def set_ab(self, ab: str):
    if not isinstance(ab, str):
      raise TypeError("AB must be a string.")
    self.__ab = ab

a = A()
b = B()

b.set_ab("di")

print(b.ab)