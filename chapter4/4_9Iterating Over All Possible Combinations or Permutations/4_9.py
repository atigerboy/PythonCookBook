items = ['a', 'b', 'c']
from itertools import  permutations
for p in permutations(items): #like p(n), considered order
    print(p)

for p in permutations(items, 2):
    print(p)

from  itertools import combinations
for c in combinations(items ,3) :#like c(n), no considered order
    print(c)

for c in combinations(items , 2):
    print( c )

from itertools import  combinations_with_replacement
for c in combinations_with_replacement(items, 3):#can chose more than once
    print(c)