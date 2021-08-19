import sys

print( sys.getfilesystemencoding() )
print( sys.getdefaultencoding() )
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

import os
print( os.listdir('.') )
print( os.listdir(b'.') )

with open(b'jalapen\xcc\x83o.txt') as f:#No such file or directory: b'jalapen\xcc\x83o.txt'
    print( f.read() )