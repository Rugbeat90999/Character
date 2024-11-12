class MyClass:
  def __init__(self, data):
    self.data = data

  def __getitem__(self, index):
    return self.data[index]

  def __setitem__(self, index, value):
    self.data[index] = value

  def __delitem__(self, index):
    del self.data[index]

# Example usage
obj = MyClass([10, 20, 30])
obj[1] = 200     # Sets item at index 1
print(obj[1])    # Output: 200
del obj[1]       # Deletes item at index 1
print(obj.data)  # Output: [10, 30]
