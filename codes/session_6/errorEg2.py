# Open terminal > python3 errorEg2.py
# Start typing below commands and see the output

import sys

for arg in sys.argv[1:]:
  try:
    f = open(arg, 'r')
    print(f.read())
  except OSError:
    print('[OS error]: ', arg)
  else:
    print(arg, 'has', len(f.readline()), 'lines')
    f.close()