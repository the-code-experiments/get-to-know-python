# Open terminal > python3 classEg6.py
# Start typing below commands and see the output

class A:
  name = 'A'

  def getName(self):
    return self.name

class B(A):
  name = 'B' # Override class A's name

  def getName(self):
    return self.name

b = B()

print(b.getName())
