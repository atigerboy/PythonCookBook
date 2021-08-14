def count(n):
    while True:
        yield  n
        n += 1

#Now using islice()
import itertools

for x in itertools.islice(count(0), 10, 20):
    print( x )