try:
  raise NameError('Hi There! I am raising an error!')
except NameError:
  print('An exception occured!')
  raise