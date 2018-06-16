# Open terminal > python3 inputOutput.py
# Start typing below commands and see the output

x = 10 * 45
y = 20 * 90

s = 'The value of x is ' + repr(x) + ' , and y is ' + repr(y)

print(s)

for a in range(1, 10):
  print(repr(a).rjust(2), repr(a*a).rjust(3), end=' ')
  print(repr(a*a*a).rjust(4))

print('\n\n')

for b in range(1, 10):
  print('{0:2d} {1:3d} {2:4d}'.format(b, b*b, b*b*b))

print('\n\n')

import math
print('The value of PI is approximately %5.3f' % math.pi)

print('I love working on {} as well as {}!'.format('JavaScript', 'Python'))

print('I love working on {0} as well as {1}!'.format('JavaScript', 'Python'))

print('I love working on {1} as well as {0}!'.format('JavaScript', 'Python'))

print('My name is {name}, and I\'am a {job}'.format(name='Ashwin', job='Software Engineer'))

print('My name is {name}, and I love working in {0}, and {1}'.format('JavaScript', 'Python', name='Ashwin'))

table = {'Ashwin': 'Engineer', 'Saju': 'Architect', 'Ajay': 'Manager'}

for name, role in table.items():
  print('{0:10} -> {1:10s}'.format(name, role))