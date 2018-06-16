# Open terminal > python3 seekTell.py
# Start typing below commands and see the output

f = open('sample.txt', 'r')

f.seek(8, 0) # 0 mean beginning of the file
print(f.read())

print('\n\n')

# f.seek(8, 1) # 1 mean current position
# print(f.read())

# print('\n\n')

# f.seek(-3, 2) # 2 mean end of the file
# print(f.read())

