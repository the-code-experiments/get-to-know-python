# Open terminal > python3 classEg8.py
# Start typing below commands and see the output

class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]

r = Reverse('XYZ')

for char in r:
  print(char)