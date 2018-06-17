# Open terminal > python3 classEg3.py
# Start typing below commands and see the output

class Person:
  actions = []

  def addAction(self, action):
    self.actions.append(action)

p1 = Person()

p1.addAction('Eating')
p1.addAction('Walking')
p1.addAction('Sleeping')

print(p1.actions)