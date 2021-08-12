x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print( x * 2 )

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print( ax * 2, ax+2 ,ax + ay, ax * ay )

def f(x):
    return 3*x**2 - 2*x+7

print( f(ax) )
print( np.sqrt( ax ) )
print( np.cos(ax) )

grid = np.zeros( shape=(10000,10000),dtype=float )
print(grid)
grid += 10
print( grid )
print( np.sin(grid) )

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
#a row 1,start at 0
print(a[1])
#a column 1,start at 0
print(a[:,1])
print(a[1:3,1:3])
# Select a subregion and change it
a[1:3,1:3] += 10
print( a )

# Broadcast a row vector across an operation on all rows
print( a + [100, 101, 102, 103])
# Conditional assignment on an array
# if all the array are 1-D ,where is equivalent to :
#[xv if c else yv for c, xv,yv in zip( condition, x, y)]
print( np.where(a<10,a, 10))
"""
[[ 1  2  3  4]
 [ 5 10 10  8]
 [ 9 10 10 10]]
"""