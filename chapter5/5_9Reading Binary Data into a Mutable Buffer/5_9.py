items = ['Hello', 'world', 'welcome', 'home', 'to', 'day']
from itertools import combinations
import gzip
with gzip.open('somefile.gz', 'wt',compresslevel=5 ) as f:
    for i in combinations(items, 2):
        print(i, file=f)

RECORD_SIZE = 32

buf = bytearray( RECORD_SIZE )
with open('somefile.gz','rb') as f:
    while True:
        n = f.readinto(buf)
        print( buf )
        if n < RECORD_SIZE:
            break