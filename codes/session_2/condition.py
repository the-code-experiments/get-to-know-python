# Open terminal > python3 condition.py
# Start typing below commands and see the output

x = int(input('Please enter an integer: '))

if x < 0:
  print(str(x) + ' is a negative number')
elif x == 0:
  print(str(x) + ' is zero')
else:
  print(str(x) + ' is a positive number')