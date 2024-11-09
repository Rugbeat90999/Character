class A:
  def __init__(self):
    self.a = 1
  
  def set_a(self, value):
    self.a = value

class B:
  def __init__(self):
    self.b = 2
  
  def set_b(self, value):
    self.b = value


class C(A, B):
  def __init__(self):
    super().__init__()
    self.c = 3
  
  def set_c(self, value):
    self.c = value

c = C()
print(c.a)