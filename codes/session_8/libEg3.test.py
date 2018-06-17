# How to Run? Open Terminal> python3 libEg3.test.py
# Read the code comments and output on the terminal

# Objective: Know about standard built-in library

# The unittest module is not as effortless as the doctest module, 
# but it allows a more comprehensive set of tests to be maintained in a separate file

import unittest
from libEg3 import average

class TestStatisticalFunctions(unittest.TestCase):

  def test_average(self):

    self.assertEqual(average([10, 20, 30]), 20)

    with self.assertRaises(ZeroDivisionError):
      average([])

    with self.assertRaises(TypeError):
      average(20, 30, 70)

unittest.main()