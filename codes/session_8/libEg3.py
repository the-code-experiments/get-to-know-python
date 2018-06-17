# How to Run? Open Terminal> python3 libEg3.py
# Read the code comments and output on the terminal

# Objective: Know about standard built-in library

# Doctest
# The doctest module provides a tool for scanning a module 
# and validating tests embedded in a programs docstrings.
# Try changing '20' in below example to see the doctest

def average(values):
  """Computes the arithmetic mean of a list of numbers
  >>> print(average([10, 20, 30]))
  20
  """
  return sum(values) / len(values)

import doctest
doctest.testmod()

# Also, see libEg3.test.py file for unittest module example