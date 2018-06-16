# Open terminal > 
#   python3 module.py
#   python3 module.py <String>
# Start typing below commands and see the output

# Import module
from message import hello, welcome
# from message import *
# import message # then use as message.hello

print(hello('Ashwin'))
print(welcome('Ashwin'))

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    hello(sys.argv[1])
  else:
    hello('Unknown')
