with open('somefile','wt') as f:
    f.write("Hello World\n")

try:
    with open('somefile','xt') as f:#x means exist
        f.write("Hello World\n")
except Exception as e:
    print( e )

import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write("Hello World\n")
else:
    print('File already exists!')