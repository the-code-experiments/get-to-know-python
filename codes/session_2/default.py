# Open terminal > python3 default.py
# Start typing below commands and see the output

# Function with default values for arguments, and while loop examples
# Note: The default value is evaluated only once.

def askme(prompt, retries=3, reminder='Invalid response, please try again!'):
  while True:
    ok = input(prompt)

    if ok in ('y', 'yes'):
      return True
    
    if ok in ('n', 'no'):
      return False
    
    retries = retries - 1

    if retries < 0:
      raise ValueError('System is auto locked!')

    print(reminder)

askme('Are you sure you want to quit? ')


# Annotations example
def hello(name: str) -> str:
  print('Annotations: ', hello.__annotations__)

hello('Ashwin')