# Warning The marshal module is not intended to be secure against erroneous or maliciously constructed data. 
# Never unmarshal data received from an untrusted or unauthenticated source.

# Marshal is not a general “persistence” module. 
# For general persistence and transfer of Python objects through RPC calls, 
# see the modules pickle and shelve. 
# 
# The marshal module exists mainly to support reading and writing the “pseudo-compiled” 
# code for Python modules of .pyc files.

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
import marshal

# Dump Python Object to marshalEg1.marshal (Binary format)
# using dump() function
with open('marshalEg1.marshal', 'wb') as writeFile:
  marshal.dump(data, writeFile)

# Read data from Pickle's Binary file
with open('marshalEg1.marshal', 'rb') as readFile:
  readData = marshal.load(readFile)
  print('Marshal binary content: ', readData)