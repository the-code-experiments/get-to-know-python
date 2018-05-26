# Open terminal > python3
# Start typing below commands and see the output

a = [10, 20, 30, 40, 50]
a # [10, 20, 30, 40, 50]
a[0] # 10
a[3] # 40
a[-1] # 50
a[0:3] # [10, 20, 30]
a[3:5] # [40, 50]
a[3:] # [40, 50]
a[:2] # [10, 20]
a[-2:] # [40, 50]
a[:-2] # [10, 20, 30]

a + [60, 70, 80, 90, 100]

a[2] = 300 
a # [10, 20, 300, 40, 50]

a.append(250)
a # [10, 20, 300, 40, 50, 250]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# Replace some value in letters list
letters[2:4] = ['C', 'D', 'E']
letters # ['a', 'b', 'C', 'D', 'E', 'e', 'f', 'g']

# Remove them
letters[2:4] = []
letters

# Clear list
letters[:] = []
letters # []

# Nested list
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b]
x # [[1, 2, 3], [4, 5, 6]]
x[0] # [1, 2, 3]
x[0][1] # 2






