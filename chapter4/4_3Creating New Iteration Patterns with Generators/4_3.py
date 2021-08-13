import cmath

def frange( start , stop, increment):#forward direction, start < stop match
    x = start
    while x < stop:
        yield  x
        x += increment
for n in frange( 0,5,0.5):
    print( n )

def frangeCorrected( start , stop, increment):
    x = start
    while ( increment >= 0 and x < stop)  or ( x > stop):
        yield  x
        x += increment

for n in frangeCorrected( 0,5,0.5):
    print( n )

for n in frangeCorrected( 5,0,-0.5):
    print( n )

def countdown(n):
    print( 'starting to count from', n)
    while n>0:
        yield  n
        n -= 1
    print( 'Done!')

c = countdown(5)
print( c )

print( next( c ) )
print( next( c ) )
print( next( c ) )
print( next( c ) )
print( next( c ) )
print( next( c ) )