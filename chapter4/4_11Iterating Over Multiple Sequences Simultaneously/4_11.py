xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):# short
    print( x, y)

from itertools import zip_longest

for x, y in zip_longest( xpts, ypts, fillvalue=0):
    print( x, y )

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict( zip(headers, values))
print( s )

a=[1,2,3]
b=[10,11,12]
c=['x','y','z']
for i in zip( a, b,c):
    print( i )

d = zip(a,b)
print( list(d))
print( list(d)) #empty only use once~