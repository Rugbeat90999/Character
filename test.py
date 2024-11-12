class A:
  def __init__(self):
    self.a = ["a"]

class B:
  def __init__(self, c: A):
    self.b = "b"
    self.c = c
  
  def test(self):
    print(f"In B: {self.c.a}")


a = A()
b = B(a)
b.test()
a.a.append("aa")
b.test()