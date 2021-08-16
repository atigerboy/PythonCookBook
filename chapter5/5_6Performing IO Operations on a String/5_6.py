import io

s = io.StringIO()
s.write('Hello world\n')
print( 'This is a test', file = s )
# s.write(b'binary data') #insert different type,error!!

print( s.getvalue() )
print( s.getvalue(),type( s.getvalue() ) )

s = io.StringIO('Hello\nWorld\n')
print( s.read(4) )
print( s.read()  )

s = io.BytesIO()
s.write(b'binary data')
print( s.getvalue(),type( s.getvalue() ) )

