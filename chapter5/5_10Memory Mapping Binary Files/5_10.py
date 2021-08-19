import os
import mmap

def memory_map( filename, access=mmap.ACCESS_WRITE ):
    size = os.path.getsize( filename )
    fd = os.open( filename, os.O_RDWR )
    return mmap.mmap( fd, size , access = access )

#create file and expand it to a desired size
size = 100000
with open('data.bin', 'wb' ) as f:
    f.seek(size -1 )
    f.write(b'\x00')

m = memory_map('data.bin')
print( len( m ) )
print( m[0:10] )
m[0:11] = b'hello world'
m.close()
print( m.closed )

with open( 'data.bin', 'rb' ) as f:
    print( f.read(11) )