import gzip

items = ['Hello', 'world', 'welcome', 'home', 'to', 'day']
from itertools import combinations_with_replacement

with gzip.open('somefile.gz', 'wt',compresslevel=5 ) as f:
    for i in combinations_with_replacement(items, 5):
        print(i, file=f)

import bz2
with bz2.open('somefile.bz2', 'wt',compresslevel=5 ) as f:
    for i in combinations_with_replacement(items, 5):
        print(i, file=f)

import os
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
    print( text )

with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
    print( text )
