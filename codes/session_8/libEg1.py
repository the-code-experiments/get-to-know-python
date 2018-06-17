# How to Run? Open Terminal> python3 libEg1.py
# Read the code comments and output on the terminal

# Objective: Know about standard built-in library

# Note: avoid using 'from os import *'.
# This will keep 'os.open()' from shadowing the built-in 'open()' function
import os

# Return the currect directory
print('Current Directory: ', os.getcwd())

# Run command mkdir in the system shell
# Return '0' means directory got created successfully
# Return '256' means directory got created failed because its already exists
print('Create directory "temp": ', os.system('mkdir temp'))

# Change current working directory
print('Change currect directory to "temp": ', os.chdir('temp'))

print('\n')

# Return a list of all module functions
print('List of all module functions: ', dir(os))

print('\n')

# System libraries
import sys

# Arguments are stored in the sys module's argv attributes as a list
print('Argv list: ', sys.argv) # python3 libEg1.py Hello => ['libEg1.py', 'hello']

print('\n')

# Output
sys.stdout.write('[STDOUT]: This is ok\n')

# Error output redirection and program termination
sys.stderr.write('[STDERR]: This is not ok\n')

print('\n')

# Mathematics
import math

print( math.cos(math.pi / 4) )
print( math.log(1024, 2) )

print('\n')

# Random
import random

print('Random choice: ', random.choice(['JavaScript', 'Python', 'Go']) ) # execute multiple times to see the output

# Statistics
import statistics

data = [2.5, 1.57, 4.32, 5.67, 8.45]
print('Statistics mean: ', statistics.mean(data) )

