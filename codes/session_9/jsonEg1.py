# How to Run? Open Terminal> python3 jsonEg1.py
# Read the code comments and output on the terminal

# Objective: Know about JSON in Python using 'json' module

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
import json

# Dump Python Object to jsonEg1.json in JSON format
# using dump() function
with open('jsonEg1.json', 'w') as writeFile:
  json.dump(data, writeFile)

print('\n')

# using dumps() function
jsonData = json.dumps(data, indent=2)
print('Data in JSON format: ', jsonData)

print('\n')

# Read data from JSON file
with open('jsonEg1.json', 'r') as readFile:
  readData = json.load(readFile)
  print('JSON file content: ', readData)
