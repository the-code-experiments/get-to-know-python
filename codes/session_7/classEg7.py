# Open terminal > python3 classEg7.py
# Start typing below commands and see the output

class A:
  name = 'A'

  def getName(self):
    return self.name

class B:
  name = 'B'

  def getName(self):
    return self.name

class C(A, B):
  name = 'C' # C Override A Override B

  def getName(self):
    return self.name

c = C()

print(c.getName())
