import sys


def bad_filename( filename ):
    return repr(filename)[1:-1]
def bad_filename2( filename ):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')
size = 10000
with open('b\udce4d.txt', 'wb' ) as f:
    f.seek(size -1 )
    f.write(b'\x00')

with open('foo.txt', 'wt' ) as f:
    f.seek(size -1 )
    f.write('\n')

import os
files = os.listdir('.')
print( files )

for name in files:
    try:
        print( name )
    except UnicodeEncodeError:
        print( bad_filename( name ))


for name in files:
    try:
        print( name )
    except UnicodeEncodeError:
        print( bad_filename2( name ))