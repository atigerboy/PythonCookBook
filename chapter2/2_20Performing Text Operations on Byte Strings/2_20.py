data=b'Hello world'
print( data[0:5] )
print( data.startswith(b'Hello') )
print( data.split())
print( data.replace(b'Hello',b'Welcome'))

barr_data = bytearray(b'Hello world')
print( barr_data[0:5] )
print( barr_data.startswith(b'Hello') )
print( barr_data.split())
print( barr_data.replace(b'Hello',b'Welcome'))

import re
data = b'FOO:BAR,SPAM'
print( re.split(b'[:,]',data) )
print( data.decode('ascii'))

print( '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii') )
