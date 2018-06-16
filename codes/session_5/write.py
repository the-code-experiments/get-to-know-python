# Open terminal > python3 write.py
# Start typing below commands and see the output

fw = open('hello.txt', 'a')
totalWrittenChar = fw.write('\nPython is needed for scripting, Machine Learning and Quantum Programming')
print('Total written characters are ' + repr(totalWrittenChar))
fw.close()

with open('hello.txt') as fr:
  data = fr.read()
  print(data)
fr.close()