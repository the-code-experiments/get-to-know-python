# How to Run? Open Terminal> python3 pickleEg1.py
# Read the code comments and output on the terminal

# Objective: Know about JSON in Python using 'pickle' module

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

# Dump Python Object to jsonEg1.json in JSON format
# using dump() function
with open('pickleEg1.pickle', 'wb') as writeFile:
  pickle.dump(data, writeFile)

print('\n')

# Read data from JSON file
with open('pickleEg1.pickle', 'rb') as readFile:
  readData = pickle.load(readFile)
  print('Pickle file content: ', readData)
