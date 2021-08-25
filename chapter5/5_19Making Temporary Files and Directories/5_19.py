from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello world\n')
    f.write('Testing\n')

    #seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    #test
    print( data )

from tempfile import NamedTemporaryFile
with TemporaryFile('w+t') as f:
    print('file name is :', f.name )


from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is :', dirname)

import  tempfile
print( tempfile.mkstemp() )
print( tempfile.mkdtemp() )
print( tempfile.gettempdir() )