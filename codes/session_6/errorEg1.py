# Open terminal > python3 errorEg1.py
# Start typing below commands and see the output

while True:
  try:
    x = int(input('Please enter a number: '))
    break
  except ValueError:
    print('Invalid number, please try again')