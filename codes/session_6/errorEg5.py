def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print('Division by zero!')
  else:
    print('result is ', result)
  finally:
    print('executing finally clause')

divide(45, 5)

divide(45, 0)