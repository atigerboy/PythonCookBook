s = b'Hello World'
import base64

a = base64.b64encode( s )
print( a )
print( base64.b64decode( a ))