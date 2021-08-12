import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print( m )
#transpose
print( m.T )
#inverse
print( m.I )
#vector
v = np.matrix([[2],[3],[4]])
print( v )

print( m * v )

import numpy.linalg

#determinant
print(numpy.linalg.det( m ))

#Eigenvalues
print( numpy.linalg.eigvals( m ) )

#solve x for mx=v
x = numpy.linalg.solve( m,v)
print( x )
print( m * x )
