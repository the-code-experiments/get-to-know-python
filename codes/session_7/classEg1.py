# Open terminal > python3 classEg1.py
# Start typing below commands and see the output

def scopeTesting():
  def doLocal():
    name = '(Do not change) -> LOCAL'
    print(name)

  def doNonLocal():
    nonlocal name # Change the name binding to scopeTesting's level
    name = '-> Changed to NON-LOCAL' 
  
  def doGlobal():
    global name # Change the name binding to module level
    name = '-> Changed to GLOBAL'

  name = "-> (Do not Change) DEFAULT" # Default, DO NOT change the name binding to scopeTesting's level"

  doLocal()
  print('After local assignment: ', name)

  doNonLocal()
  print('After non-local assignment: ', name)

  doGlobal()
  print('After global assignment: ', name)

scopeTesting()
print('In global scope: ', name)