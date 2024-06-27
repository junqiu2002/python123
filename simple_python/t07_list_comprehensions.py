
# : List comprehensions is also called  shortcut for a for loop
#• Shortcut for a for loop
#• Optional if clause
#• Always returns list
#• Syntax
#    [ EXPR for VAR in SEQUENCE if EXPR ]

#results = []
#for var in sequence:
#  results.append(expr) # where expr involves var

# the above can be re-written as:
#  results = [ expr for var in sequence ]

# A conditional if may be added:
#results = [ expr for var in sequence if expr ]

## The loop expression can be a tuple. You can nest two or more for loops.

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']
ufruits = [fruit.upper() for fruit in fruits]

afruits = [fruit.title() for fruit in fruits if fruit.startswith('a')]

print("ufruits:", ufruits)
print("afruits:", afruits)
print()

values = [2, 42, 18, 39.7, 92, '14', "boom", ['a', 'b', 'c']]
doubles = [v * 2 for v in values]
print("doubles:", doubles, '\n')

nums = [x for x in values if isinstance(x, int)]
print(nums, '\n')
dirty_strings = [' Gronk ', 'PULABA ', ' floog']
clean = [d.strip().lower() for d in dirty_strings]
for c in clean:
  print(">{}<".format(c), end=' ')
print("\n")

suits = 'Clubs', 'Diamonds', 'Hearts', 'Spades'
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [(rank, suit) for suit in suits for rank in ranks]

for rank, suit in deck:
 print("{}-{}".format(rank, suit))


