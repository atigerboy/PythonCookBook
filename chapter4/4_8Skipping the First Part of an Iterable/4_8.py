from itertools import  islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

with open('AnimatedFire.shader') as f:
    while True:
        line = next(f, None)
        if line == None or line.startswith('/*ASEBEGIN'):#contain '\n' so use == failed
            break
    #process remaining lines
    while line:
        print( line, end='')
        line = next(f,None)

