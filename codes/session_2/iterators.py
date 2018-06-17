# Open terminal > python3 iterators.py
# Start typing below commands and see the output

for element in [1, 2, 3]:
  print(element)

for element in (1, 2, 3):
  print(element)

for key in { 'one': 1, 'two': 2, 'three': 3}:
  print(key)

for char in '123':
  print(char)

print('\n\n')

s = 'XYZ'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # StopIteration Exception