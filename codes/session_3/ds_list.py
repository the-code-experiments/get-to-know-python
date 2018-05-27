# Open terminal > python3 ds_list.py (Data Structure)
# Start typing below commands and see the output

birds = ['Owl', 'Macaw', 'Parrot', 'BeeHumming']

# Return the number of x appears in the list
print('\nCount: ' + str(birds.count('Macaw')))

# Return zero-based index in the list, Raises a ValueError if no item exist
print('\nIndex: ' + str(birds.index('Parrot')))

# Reverse the elements of the list in place
print('\nReverse: ')
birds.reverse()
print(birds)

# Sort
print('\nSort: ')
birds.sort()
print(birds)

# Append
print('\nAppend Penguin')
birds.append('Penguin')
print(birds)

# Insert
print('\nInsert Kingfisher on index 3')
birds.insert(3, 'Kingfisher')
print(birds)

# Pop
print('\nPop bird on index 3')
birds.pop(3)
print(birds)

# Remove
print('\nRemove bird Penguin')
birds.remove('Penguin')
print(birds)

# clear
print('\nClear birds list')
birds.clear()
print(birds)

