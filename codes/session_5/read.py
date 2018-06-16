# Open terminal > python3 read.py
# Start typing below commands and see the output

with open('hello.txt') as f:
  data = f.read()
  print(data)
f.closed