# How to Run? Open Terminal> python3 pickleEg1.py
# Read the code comments and output on the terminal

# Objective: Know about JSON in Python using 'pickle' module

# Compare with Marshal
# https://docs.python.org/3/library/pickle.html#module-pickle

# Python Object
data = {
  "empId": 1,
  "name": {
    "first": "Ashwin",
    "last": "Hegde"
  },
  "email": "ashwin.hegde3@gmail.com",
  "isEngineer": True
}

# Built-in JSON library
import pickle

# Dump Python Object to pickleEg1.pickle (Binary format)
# using dump() function
with open('pickleEg1.pickle', 'wb') as writeFile:
  pickle.dump(data, writeFile)

# Read data from Pickle's Binary file
with open('pickleEg1.pickle', 'rb') as readFile:
  readData = pickle.load(readFile)
  print('Pickle binary content: ', readData)
