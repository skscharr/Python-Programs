# SetCombo.py

# This program will take a variable number of lists and return
# a single random selection from each list in the order the lists
# are passed to the function. The function must account for lists
# of variable lengths.

import random

l1 = [ 'apple', 'banana', 'pear' ]
l2 = [ 'car', 'truck' ]
l3 = [ 'zambia', 'malawi', 'kenya' ]
l4 = [ 'cat', 'dog', 'hamster', 'fish' ]

def combo(*lists):
    new = []
    for x in range(len(lists)):
        n = random.randrange(len(lists[x]))
        new.append(lists[x][n])
    return ', '.join(new)

print combo(l1, l2, l3, l4)
