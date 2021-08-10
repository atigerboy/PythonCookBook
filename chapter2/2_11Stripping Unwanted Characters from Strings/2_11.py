s = ' hello world \n'
print( s.strip() )
print( s.lstrip() )
print( s.rstrip() )

t = '-----hello====='
print( t.lstrip('-'))
print( t.rstrip('='))
print( t.strip('-='))

s = ' hello world \n'
print( s.strip( ))

print( s.replace(' ', '') )
import re
s = '   hello         world     \n'
print( re.sub('\s+',' ', s))
