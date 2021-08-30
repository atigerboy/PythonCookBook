'''This feature is easy to implement if you place the keyword arguments after a  * argument
or a single unnamed  * '''

def recv(maxsize, *, block):
    'Receives a message'
    pass

#recv(1024, True) #TypeError
recv( 1024, block=True )

def mininum( *values, clip=None):
    m = min( values )
    if clip is not None:
        m = clip if clip>m else m
    return m

print( mininum(1, 5, 2, -5, 10) ) # Returns -5
print( mininum(1, 5, 2, -5, 10, clip=0) ) # Returns 0

print( help( recv ))
print( help( mininum ) )