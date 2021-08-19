items = ['Hello', 'world', 'welcome', 'home', 'to', 'day']
from itertools import combinations
import gzip
with gzip.open('somefile.gz', 'wt',compresslevel=5 ) as f:
    for i in combinations(items, 2):
        print(i, file=f)

from functools import partial
RECORD_SIZE = 32

with open('somefile.gz','rb') as f:
    records = iter( partial( f.read, RECORD_SIZE),b'')
    for r in records:
        print( r )
