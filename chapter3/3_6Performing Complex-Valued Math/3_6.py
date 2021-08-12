a = complex(2, 4)
b = 3-5j
print( a, type(b))
print( a.real, a.imag)
print( a.conjugate() )
print( a + b )
print( a * b )
print( a / b )

print( abs(a) )

import cmath
print( cmath.sin(a) )
print( 'test=============={')
print( cmath.sin(a.real)*cmath.cosh(a.imag) ,'+', cmath.cos(a.real)*cmath.sinh(a.imag),'j' )
print( 'test==============}')
print( cmath.cos(a) )
print( cmath.exp(a) )
print( cmath.sqrt( -1 ) )


import numpy as np
a = np.array([2+3j,4+5j,6-7j,8+9j])
print( a )
print( a + 2 )
print( np.sin(a) )# sin(a.real),sin(a.image)