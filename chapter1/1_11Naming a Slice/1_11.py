import random
record=''.join([str(random.randint(0,9)) for i in range(100)])
SHARES=slice(20,25) #only use magic number once
PRICE = slice(37,42)

cost= int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print( items[a])
items[a]=[10,11]
print( items )

del items[a]
print( items )

#slice have start, stop ,step
a = slice(10,50, 2)
print( a.start, a.stop, a.step )

#use indices(size) to remap
s = 'HelloWorld'

print(a.indices(len(s))) #return a tuple not a slice object
#(10, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i],end='')