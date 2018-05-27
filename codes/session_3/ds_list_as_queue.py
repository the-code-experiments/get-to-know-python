# Open terminal > python3 ds_list_as_stack.py (Data Structure)
# Start typing below commands and see the output

# Stack:
# First-in First-out

# Import collection.deque
from collections import deque

queue = deque(['Owl', 'Macaw', 'Parrot', 'BeeHumming'])

# First-in
print('\nFirst-in: ')
queue.append('Kingfisher')
queue.append('Penguin')
print(queue)

print('\nFirst-out: ')
print(queue.popleft()) # Owl
print(queue.popleft()) # Macaw
print(queue)
