# Open terminal > python3
# Start typing below commands and see the output

# Use single quote
'Ashwin'

'Ashwin\'s'

# Use double quote
"Ashwin's"

"Hello \"Ashwin\" "

name = 'Ashwin Hegde\nashwin.hegde3@gmail.com'
name # Without print() => \n has no effect
print(name) ## \n means new line

print('C:\python\name')
print(r'C:\python\name') # r before single quote

# String in multi line, 1 way using triple-quotes """...""" or '''...'''
print("""\
  Usage: python-cli [options]
      -h help
      -H hostname
""")

# String can be concate using +
'Ashwin' + 'Hegde'

# 2 or more string only (no variable or no expression) kept next to each other are automatically concate
'Ash' 'win' ' ' 'Hegde'

# String can be repeat using *
'Ashwin will' + 3 * ' Win'

# Handling long strings
text = ('Hello World! My name is Ashwin '
        'and we are learning Python Syntax!')
text

# String index (starts from left)
# and negative index (starts from right and from -1)
name = 'Ashwin'
name[0] # A
name[5] # n
name[7] # IndexError: String index out of range
name[-1] # n
name[-3] # w

# Slicing
name[3:6] # win => 3 included, 6 excluded
name[3:] # win
name[:3] # Ash

# How Slice works?
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# String length
len('Ashwin') # 6

