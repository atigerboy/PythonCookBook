from collections.abc import Iterable

def flattern( items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield  from flattern( x )
        else:
            yield x

items =  [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flattern( items ):
    print( x )