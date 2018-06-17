# Open terminal > python3 classEg5.py
# Start typing below commands and see the output

# Base class
class Person:
  actions = []
  
  # def __init__(self):
  #   self.actions = []  # Cannot be accessed from Derived class instance

  def addActions(self, action):
    self.actions.append(action)

# Derived class
class Student(Person):
  def __init__(self):
    self.name = 'Ashwin'

  def getName(self):
    return 'My name is ' + self.name

s1 = Student()
print(s1.getName())

s1.addActions('Eating')
s1.addActions('Sleeping')
print(s1.actions)