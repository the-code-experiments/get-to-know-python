# packing
def add(*numbers):
  total = 0
  for num in numbers:
    total = total + num
  return total

print(add(2, 3))
print(add(2, 3, 4))
