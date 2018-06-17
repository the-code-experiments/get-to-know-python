# How to Run? Open Terminal> python3 libEg2.py
# Read the code comments and output on the terminal

# Objective: Know about standard built-in library

# Dates and Times
from datetime import date

# Get today's date
now = date.today()
print("Today's date: ", now)

# Set date
customDate = date(2000, 12, 2)
print("Custom date: ", customDate)

print('\n')

# Data compression
import zlib

print('Data Compression Try 1: \n')

dataStr1 = b'Hello world! my name is Ashwin' # prefix 'b' means bytes-like object
print('Original: ', len(dataStr1) )

comDataStr1 = zlib.compress(dataStr1)
print('Compress: ', len(comDataStr1) )

deComDataStr1 = zlib.decompress(comDataStr1)
print('Decompress: ', len(deComDataStr1) )

print('\n')

print('Data Compression Try 2: \n')

dataStr2 = b'Ashwin Ashwin Ashwin Ashwin' # prefix 'b' means bytes-like object
print('Original: ', len(dataStr2) )

comDataStr2 = zlib.compress(dataStr2)
print('Compress: ', len(comDataStr2) )

deComDataStr2 = zlib.decompress(comDataStr2)
print('Decompress: ', len(deComDataStr2) )

