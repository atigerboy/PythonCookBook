from decimal import  Decimal
a = Decimal( '4.2' )
b = Decimal( '2.1 ')
print( a + b )
print( a + b == Decimal('6.3') )

a = Decimal( '1.3')
b = Decimal( '1.7' )
print( a/b )
from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 3
    print( a/b )

with localcontext() as ctx:
    ctx.prec = 50
    print( a/b )

nums=[1.23e+18, 1, - 1.23e+18]
print( sum(nums) )

import math
print( math.fsum( nums ))
