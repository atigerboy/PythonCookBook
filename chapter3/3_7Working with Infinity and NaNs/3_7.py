a = float('inf')
b = float('-inf')
c = float('nan')

print( a == -b, a/b, a+b )
print( a>0, a<0, a==0 )
print( c>0, c<0, c==0 )
import math
print( math.isinf( a ), math.isnan( a ))
print( math.isinf( c ), math.isnan( c ))
d = float( 'nan' )
print( c == d, c is d )
