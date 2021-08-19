import os

print( os.path.exists( __file__ ) )
print( os.path.isfile( __file__ ) )

print(os.path.isdir( os.path.relpath('.')))
#symoblic link~~



print( os.path.getsize( __file__))
print(os.path.getmtime( __file__))

import time
print( time.ctime( os.path.getmtime(__file__)))