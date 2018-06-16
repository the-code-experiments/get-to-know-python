def thisWillFail():
  x = 1 / 0

try:
  thisWillFail()
except ZeroDivisionError as err:
  print('Handling runtime error: ', err)