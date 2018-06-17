# Open terminal > python3 classEg4.py
# Start typing below commands and see the output

class Person:
  def __init__(self):
    self.actions = []

  def addActions(self, action):
    self.actions.append(action)
  
p1 = Person()

p1.addActions('Eating')
p1.addActions('Sleeping')

print(p1.actions)